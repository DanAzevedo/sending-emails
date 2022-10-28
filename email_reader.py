from imbox import Imbox
from datetime import datetime
import pandas as pd

username = 'daniel.danilove@gmail.com'
password = open('pass.txt', 'r').read()
# Servidor imap
# https://support.pipedrive.com/pt/article/how-can-i-find-my-imap-and-smtp-information
host = 'imap.gmail.com'

mail = Imbox(host, username=username, password=password, ssl=True)
messages = mail.messages(unread=True)
print(len(messages))
for (uid, message) in messages:
    message.subject
    message.body
    message.sent_from
    message.sent_to
    message.cc
    message.headers
    message.date

    if len(message.attachments) > 0:
        for attach in message.attachments:
            file = open('attachment/report.pdf', 'wb')
            attach['content'].seek(0)
            file.write(attach['content'].read())
            file.close()
