#!/usr/bin/env python
from __future__ import unicode_literals
import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
from ftp_backend import FTPBackend
import pdb
history = InMemoryHistory()
hostname = username = None
hostname = sys.argv[1]
if "@" in hostname:
    username, hostname = hostname.split("@")

password = prompt('password: ', is_password=True)
username = username or None
connection = FTPBackend(hostname, username, password)

while True:
    ret = ''
    completer = WordCompleter(connection.parse('listdir'))
    if username:
        prmt = '{}@'.format(username)
    else:
        prmt = ''
    prmt += '{}:{}$ '.format(hostname, connection.parse('pwd'))
    text = prompt(prmt, history=history, completer = completer, complete_while_typing=False)
    ret = connection.parse(text)
    if ret:
        print ret
