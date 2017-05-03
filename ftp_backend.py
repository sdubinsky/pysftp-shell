import pysftp
import pdb
class FTPBackend(object):
    def __init__(self, hostname, username, password):
        self.connection = pysftp.Connection(hostname, username=username, password=password.strip())

    def parse(self, command):
        words = command.split()
        command = words[0]
        if len(words) > 1:
            params = " ".join(words[1:])
        else:
            params = None
        try:
            fn = getattr(self.connection, command, None)
            if fn:
                if isinstance(fn, basestring):
                    print fn
                    return
                if params:
                    ret = fn(params)
                else:
                    ret = fn()
                if ret:
                    print ret
            else:
                raise Exception("Error: {} is not a valid function".format(command))
        except Exception as e:
            print e.message

