import rsa


def encryptDoc(doc):
    (pubkey, privkey) = rsa.newkeys(512)
    # might have to encode doc first
    encodedDoc = doc.encode('utf-8')
    return {"ecryptedDoc": rsa.encrypt(encodedDoc, pubkey), "privateKey": privkey}
