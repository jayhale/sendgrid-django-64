import os

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.test import SimpleTestCase as TestCase
from sgbackend import SendGridBackend

settings.configure(SENDGRID_API_KEY=os.environ.get('SENDGRID_API_KEY'))


class Issue64Tests(TestCase):
    def test_reply_to_header(self):
        backend = SendGridBackend()

        mail = EmailMultiAlternatives(
            subject='Your subject',
            body='Simple text body',
            from_email='webmaster@dummydomain.com',
            to=['recipient@dummydomain.com',],
            headers={'Reply-To': 'replyto@dummydomain.com'}
            )

        # Replicate backend sending
        prepared_mail = backend._build_sg_mail(mail)

        # Check for propper assembly
        self.assertEqual(
            prepared_mail,
            {
                'from': {'email': 'webmaster@dummydomain.com'},
                'subject': 'Your subject',
                'personalizations': [{
                    'to': [{'email': 'recipient@dummydomain.com'}],
                    'subject': 'Your subject'
                }],
                'content': [{'type': 'text/plain', 'value': 'Simple text body'}],
                'reply_to': {'email': 'replyto@dummydomain.com'}
            }
        )

        # Send to SendGrid
        response = backend.sg.client.mail.send.post(request_body=prepared_mail)
        self.assertEqual(
            response.status_code,
            202
        )


    def test_reply_to_property(self):
        backend = SendGridBackend()

        mail = EmailMultiAlternatives(
            subject='Your subject',
            body='Simple text body',
            from_email='webmaster@dummydomain.com',
            to=['recipient@dummydomain.com',]
            )
        mail.extra_headers = {'Reply-To': 'replyto@dummydomain.com'}

        prepared_mail = backend._build_sg_mail(mail)

        # Check for propper assembly
        self.assertEqual(
            prepared_mail,
            {
                'from': {'email': 'webmaster@dummydomain.com'},
                'subject': 'Your subject',
                'personalizations': [{
                    'to': [{'email': 'recipient@dummydomain.com'}],
                    'subject': 'Your subject'
                }],
                'content': [{'type': 'text/plain', 'value': 'Simple text body'}],
                'reply_to': {'email': 'replyto@dummydomain.com'}
            }
        )

        # Send to SendGrid
        response = backend.sg.client.mail.send.post(request_body=prepared_mail)
        self.assertEqual(
            response.status_code,
            202
        )



