from smtplib import SMTP_SSL
import os
import traceback
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host = os.getenv('MAILLOG_HOST')
smtp_from = os.getenv('MAILLOG_FROM')
smtp_port = os.getenv('MAILLOG_PORT')
smtp_user = os.getenv('MAILLOG_USER')
smtp_pass = os.getenv('MAILLOG_PASS')

recipients = os.getenv('MAILLOG_TO')


def format_exception(e):
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(
        traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))

    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception_list)
    # Removing the last \n
    exception_str = exception_str[:-1]

    return exception_str


def maillog(subject, msg):
    smtp = SMTP_SSL('%s:%s' % (smtp_host, smtp_port), context=None)
    smtp.login(smtp_user, smtp_pass)
    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = smtp_from
    message['To'] = recipients
    part1 = MIMEText(msg, "plain", "utf-8")
    message.attach(part1)
    smtp.sendmail(smtp_from, recipients, message.as_string())
