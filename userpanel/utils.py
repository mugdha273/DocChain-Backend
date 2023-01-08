import os
from cryptography.fernet import Fernet


def decryptDoc(doc, privkey):
    # decryptedDoc = rsa.decrypt(doc, privkey)
    # might have to decode decryptedDoc
    decodedDoc = decryptDoc.decode('utf-8')
    return decodedDoc

def encryptDoc(doc):
    # (pubkey, privkey) = rsa.newkeys(4096)
    # # might have to encode doc first
    # # encodedDoc = doc.encode('utf-8')
    # return {"ecryptedDoc": rsa.encrypt(doc, pubkey), "privateKey": privkey}
    
    # Generate a new RSA key pair
    key = Fernet.generate_key()
    f = Fernet(key)
    # encodedDoc = doc.encode('utf-8')
    encrypted = f.encrypt(doc)
    
    # print(encrypted)
    return {"ecryptedDoc": encrypted, "privateKey": key}