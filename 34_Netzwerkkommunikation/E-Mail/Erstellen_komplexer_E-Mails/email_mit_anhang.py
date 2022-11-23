#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg["Subject"] = "Hallo Welt"
msg["From"] = "Donald Duck <don@ld.de>"
msg["To"] = "Onkel Dagobert <d@gobert.de>"

text = MIMEText("Dies ist meine selbst erstellte E-Mail.")
msg.attach(text)

f = open("lena.png", "rb")
bild = MIMEImage(f.read())
f.close()
msg.attach(bild)

print(msg.as_string())
