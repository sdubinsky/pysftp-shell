from __future__ import unicode_literals
import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
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
    text = prompt('ftp$ ', history=history, auto_suggest=AutoSuggestFromHistory())
    connection.parse(text)
