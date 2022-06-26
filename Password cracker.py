import hashlib

flag = 0
Counter = 0

pass_hash = input("Enter md5 hash")

wordlist = input("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)
    Counter += 1

if digest == pass_hash:
    print ("Password found")
    print ("Password is " + word)
    print (Counter)
    flag = 1
    break

if flag == 0:
    print("Password/passphrase is not in the list")

#Run in Command Prompt (python Password cracker.py), then enter a MD5 hash from notes or somewhere else, then make the file name (Passlist.txt)