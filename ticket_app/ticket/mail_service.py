from django.core.mail import send_mail


def email_confirmation(request):
    subject = "AM Week"
    message = "Thank you for purchasing a ticket for our event!"
    from_mail = "amweek@events.com"
    recipient_list = [request.POST["email_address"]]
    send_mail(subject,
              message,
              from_mail,
              recipient_list,
              fail_silently=False)

