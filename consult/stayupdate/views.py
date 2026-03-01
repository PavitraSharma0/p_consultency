from django.shortcuts import redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import StayUpdateForm
from .models import StayUpdate

def stayupdate_view(request):
    if request.method == 'POST':
        form = StayUpdateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber, created = StayUpdate.objects.get_or_create(email=email)

            if created:
                print("✅ StayUpdate: New subscriber added — preparing to send emails")

                # Email to admin
                send_mail(
                    subject=f"New subscription from {subscriber.email}",
                    message=f"New sign-up received:\n\nEmail: {subscriber.email}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                print("📨 Admin email sent")

                # Email to subscriber
                html_content = render_to_string('partials/email_stayupdate_response.html', {'email': subscriber.email})
                email_message = EmailMultiAlternatives(
                    subject="Thank You for Subscribing!",
                    body="We have received your subscription successfully.",
                    from_email=settings.EMAIL_HOST_USER,
                    to=[subscriber.email],
                )
                email_message.attach_alternative(html_content, "text/html")
                email_message.send(fail_silently=False)
                print("📩 Subscriber email sent")

                messages.success(request, "Thank you for subscribing!")
            else:
                print("⚠️ Subscriber already exists, skipping email send")
                messages.info(request, "You're already subscribed!")

            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, "Invalid email address or Subscriber already exists . Please try again.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/')