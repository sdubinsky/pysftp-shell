# Pysftp-Shell

This is a thin wrapper over pysftp to provide a more useful shell than the standard sftp shell.  Improvements include autocomplete based on the files in the current directoy, in-memory history navigation, and arrow key usage.

Honestly it's just [prompt_toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) on the front end and [pysftp](https://bitbucket.org/dundeemt/pysftp) on the backend with some error handling in the middle.

Start it with `ftp_prompt.py $hostname $username`.  It'll ask you for a password, then you're good to go.
