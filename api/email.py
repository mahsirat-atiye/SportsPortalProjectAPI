from django.core.mail import EmailMessage

EMAIL_MESSAGES = {'success': 'با سلام. یک ورود موفق به سامانه فوتبال داشتید.',
                  'failure': 'با سلام. یک ورود ناموفق به سامانه فوتبال داشتید.',
                  'forgotten': 'با سلام. شما برای این ایمیل، یک درخواست برای دریافت کد فراموشی داشته‌اید. برروی لینک مقابل کلیک کنید: ',
                  'activation': 'با سلام. شما در سامانه فوتبال ثبت نام کردید. برای تایید حساب ایمیل، برروی لینک مقابل کلیک کنید: ',
                  }


def send_email(email, title, extra=''):
    print(email, title)
    email = EmailMessage(title, EMAIL_MESSAGES[title] + extra, to=[email])
    email.send()
