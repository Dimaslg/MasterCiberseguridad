import os
import hashlib
import requests
import uuid

def decryptapi(hash):
    req = requests.get('https://md5decrypt.net/en/Api/api.php?hash='+hash+'&hash_type=md5&email=nistinutre@vusra.com&code=27da0dbcdd7d0440')
    return (req.text)

def writefile(filename, value):
    with open(filename, 'a') as f:
        f.write(value)
    f.close()

with open(os.getcwd()+"./md5pass.txt", 'r') as md5file:
    for md5 in md5file:
        writefile( 'plainpass.txt', decryptapi(md5.strip())+"\n");
md5file.close()

with open('plainpass.txt','r') as plainpassfile:
    for plainpass in plainpassfile:
        if(plainpass != '\n'):
            salt = uuid.uuid4().hex
            writefile('sha256pass.txt',hashlib.sha256(salt.encode() + plainpass.encode('utf-8')).hexdigest() + "\n")
        else:
            writefile('sha256pass.txt',"\n")
plainpassfile.close()





