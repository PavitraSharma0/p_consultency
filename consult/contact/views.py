from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                message = form.save()
            except Exception:
                message = form.save(commit=False)
            
            send_mail(
                subject=f"New Contact Message from {message.fullname}",
                message=f"""
                        New message from the website contact form:

                        Full Name: {message.fullname}
                        Email: {message.email}
                        Subject: {message.subject}
                        Message:{message.message}
                        """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            html_content = render_to_string('partials/email_contact_response.html', {
                'fullname': message.fullname,
                'email': message.email,
                'subject': message.subject,
                'message_text': message.message,
            })

            email = EmailMultiAlternatives(
                subject="Thank You for Contacting T-Consultancy!",
                body="We have received your message successfully.",
                from_email=settings.EMAIL_HOST_USER,
                to=[message.email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})