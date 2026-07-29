from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .forms import QuoteForm

# Create your views here.

def quote_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            try:
                message = form.save()
            except Exception:
                message = form.save(commit=False)

            send_mail(
                subject=f"New Quote Request from {message.fullname}",
                message=f"""
                        New quote request received:

                        Full Name: {message.fullname}
                        Email: {message.email}
                        Service: {message.service}
                        """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            html_content = render_to_string('partials/email_quote_response.html', {
                'fullname': message.fullname,
                'email': message.email,
                'service': message.service,
            })

            email = EmailMultiAlternatives(
                subject="Thank You for Requesting Quote.",
                body="We have received your quote request successfully.",
                from_email=settings.EMAIL_HOST_USER,
                to=[message.email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return redirect('quote')
    else:
        form = QuoteForm()
    return render(request, 'quote.html', {'form': form})
