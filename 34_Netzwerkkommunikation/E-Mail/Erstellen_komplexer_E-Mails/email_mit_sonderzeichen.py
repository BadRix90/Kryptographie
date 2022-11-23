#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header

text = "39,90\u20AC"
msg = MIMEText(text.encode("cp1252"), _charset="cp1251")
msg["Subject"] = Header("39,90\u20AC", "cp1252")
msg["From"] = "Donald Duck <don@ld.de>"
msg["To"] = "Onkel Dagobert <d@gobert.de>"

print(msg.as_string())
