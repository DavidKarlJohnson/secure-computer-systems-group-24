import os

file_descriptor = os.open('secret_textfile.txt', os.O_WRONLY | os.O_CREAT)   # open a file for writing,
user_inp = input('Waiting for user input: ')                                 # stop and wait for input from the user,
os.write(file_descriptor, b"Something")                                      # write on the file descriptor,
os.close(file_descriptor)                                                    # close the file