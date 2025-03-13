'''
FTP-Server

This is the FTP Server. It is used to handle FTP protocols 

Download from Server to Client.
Upload from Client to Server.

This code is not the main code

This code is executed first before the main.py to use the FTP-Client.


'''

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer() # handle permission and user

# Allow user Anonymous and home directory having read and write permissions
authorizer.add_anonymous('./ftpServerData' , perm='elrw')

# Instantiate FTP handler class
handler = FTPHandler 
handler.authorizer = authorizer


address = ('localhost', 8088)
server = FTPServer(address, handler)

# start ftp server
server.serve_forever()