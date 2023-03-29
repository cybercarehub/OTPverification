import smtplib
import random


def generate_otp():
    """Generate a 6-digit OTP"""
    return random.randint(100000, 999999)


def send_email(to, otp):
    """Send an email with the OTP"""
    from_email = 'your_email@gmail.com'
    password = 'your_email_password'

    message = f'Subject: OTP Verification\n\nYour OTP is {otp}'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.sendmail(from_email, to, message)


def verify_otp(email):
    """Verify the OTP entered by the user"""
    otp_sent = generate_otp()
    send_email(email, otp_sent)

    print('An OTP has been sent to your email. Please enter the OTP to verify your account.')

    otp_entered = int(input('Enter OTP: '))

    if otp_entered == otp_sent:
        print('OTP verified successfully.')
    else:
        print('Incorrect OTP. Please try again.')


# Example usage
verify_otp('user@example.com')
