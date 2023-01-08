import rsa


def decryptDoc(doc, privkey):
    decryptedDoc = rsa.decrypt(doc, privkey)
    # might have to decode decryptedDoc
    decodedDoc = decryptDoc.decode('utf-8')
    return decodedDoc
