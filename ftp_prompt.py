#!/usr/bin/env python
from __future__ import unicode_literals
import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
from ftp_backend import FTPBackend

history = InMemoryHistory()
hostname = None
hostname = sys.argv[1]
if len(sys.argv) >= 3:
    username = sys.argv[2]

password = prompt('password: ', is_password=True)
username = username or None
connection = FTPBackend(hostname, username, password)

while True:
    completer = WordCompleter(connection.parse('listdir'))
    text = prompt('ftp$ ', history=history, completer = completer, complete_while_typing=False)
    ret = connection.parse(text)
    if ret:
        print ret
