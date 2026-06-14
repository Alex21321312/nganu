import base64

def encrypt(plain_text, key):
    enkripsi = ""
    panjang_key = len(key)

    for i in range(len(plain_text)):
        ascii_baru = (
            ord(plain_text[i]) +
            ord(key[i % panjang_key])
        ) % 256

        enkripsi += chr(ascii_baru)

    return base64.b64encode(
        enkripsi.encode("latin1")
    ).decode("ascii")


def decrypt(cipher_text, key):

    enkripsi = base64.b64decode(
        cipher_text.encode("ascii")
    ).decode("latin1")

    dekripsi = ""
    panjang_key = len(key)

    for i in range(len(enkripsi)):
        new_ascii_d = (
            ord(enkripsi[i]) -
            ord(key[i % panjang_key])
        ) % 256

        dekripsi += chr(new_ascii_d)

    return dekripsi