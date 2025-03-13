# '''
# FTP Client


# This is a ftp-client code. The code uses ftplib library to connect to the ftp server and
# download or upload files from the server.

# This code is executed from the main.py file.

# Please ensure that the ftp-server.py is running before running this code from main.py

# '''

# # CLIENT SIDE
# import os
# import ftplib
# print("\n******************************")
# print("Upload/Download File Using FTP")
# print("******************************")

# ftp = ftplib.FTP()
# ftp.connect('localhost', 8088)
# ftp.login()

# # function to download a file from ftpServerData to ftpClientData
# def download_file(ftp, filename):
#     try:
#         if filename not in ftp.nlst():
#             print(f'File not found: {filename}')
#             return False

#         local_file = os.path.join("ftpClientData", filename)
#         with open(local_file, 'wb') as file:
#             ftp.retrbinary("RETR " + filename, file.write)
#         print(f'Downloaded file: {filename} to ftpClientData folder.')
#         return True
#     except:
#         print(f'Error downloading file: {filename}')
#         return False

# # function to upload a file from ftpClientData to ftpServerData
# def upload_file(ftp, filename):
#     try:
#         local_file = os.path.join("ftpClientData", filename)
#         ftp.storbinary('STOR ' + filename, open(local_file, 'rb'))
#         print(f'Uploaded file: {filename} from ftpClientData folder.')
#         return True
#     except:
#         print(f'Error uploading file: {filename}')
#         return False

# # MAIN MENU FOR FILE TRANSFER
# while True:
#     print("\n[1] Download file from ftpServerData to ftpClientData")
#     print("[2] Upload file from ftpClientData to ftpServerData")
#     print("[3] Exit")
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         # Display the contents of the ftpServerData directory
#         print("\nContents of ftpServerData:")
#         print(*ftp.nlst(), sep='\n')

#         filename = input("\nEnter file name: ")
#         if download_file(ftp, filename):
#             print("Download successful.")
#         else:
#             print("Download failed.\n")
#             break

#     elif choice == '2':
#         # Display the contents of the ftpClientData directory
#         print("\nContents of ftpClientData:")
#         print(*os.listdir("ftpClientData"), sep='\n')

#         filename = input("\nEnter file name: ")
#         if upload_file(ftp, filename):
#             print("Upload successful.")
#         else:
#             print("Upload failed.\n")

#     elif choice == '3':
#         break

#     else:
#         print("Invalid choice.")

# ftp.quit()






'''
FTP Client


This is a ftp-client code. The code uses ftplib library to connect to the ftp server and
download or upload files from the server.

This code is executed from the main.py file.

Please ensure that the ftp-server.py is running before running this code from main.py

'''

# CLIENT SIDE
import os
from ftplib import FTP

# Connect to the FTP server
ftp = FTP()
ftp.connect("localhost", 8088)
ftp.login("anonymous", "")

# function to download a file from ftpServerData to ftpClientData
def download_file(ftp, filename):
    try:
        if filename not in ftp.nlst():
            print(f'File not found: {filename}')
            return False

        local_file = os.path.join("ftpClientData", filename)
        with open(local_file, 'wb') as file:
            ftp.retrbinary("RETR " + filename, file.write)
        print(f'Downloaded file: {filename} to ftpClientData folder.')
        return True
    except:
        print(f'Error downloading file: {filename}')
        return False

# function to upload a file from ftpClientData to ftpServerData
def upload_file(ftp, filename):
    try:
        local_file = os.path.join("ftpClientData", filename)
        if not os.path.exists(local_file):
            print(f'File not found: {filename}')
            return False

        with open(local_file, 'rb') as file:
            ftp.storbinary("STOR " + filename, file)
        print(f'Uploaded file: {filename} to ftpServerData folder.')
        return True
    except:
        print(f'Error uploading file: {filename}')
        return False

# MAIN MENU FOR FILE TRANSFER
while True:
    print("\n[1] Download file from ftpServerData to ftpClientData")
    print("[2] Upload file from ftpClientData to ftpServerData")
    print("[3] Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Display the contents of the ftpServerData directory
        print("\nContents of ftpServerData:")
        print(*ftp.nlst(), sep='\n')

        while True:
            filename = input("\nEnter file name: ")
            if download_file(ftp, filename):
                print("Download successful.")
                break
            else:
                print("Download failed. Please try again.")

    elif choice == '2':
        # Display the contents of the ftpClientData directory
        print("\nContents of ftpClientData:")
        print(*os.listdir("ftpClientData"), sep='\n')

        while True:
            filename = input("\nEnter file name: ")
            if upload_file(ftp, filename):
                print("Upload successful.")
                break
            else:
                print("Upload failed. Please try again.")

    elif choice == '3':
        ftp.quit()
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")