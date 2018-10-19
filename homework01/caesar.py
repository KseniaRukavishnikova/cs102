def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    cliphertext = ''
    for alp in plaintext:
        if (alp >= 'a') and (alp <= 'z') or (alp >= 'A') and (alp <= 'Z'):
            code = ord(alp) + 3
            if ord ('a') > code > ord('Z') or code > ord('z'):
                code -= 26
            cliphertext += chr(code)
        else:
            cliphertext += alp
    return cliphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for alp in plaintext:
        if (alp >= 'a' and alp <= 'z') or (alp >= 'A' and alp <= 'Z'):
            code = ord(alp) + 3
            if ord ('a') > code > ord('Z') or code > ('z'):
                code -= 26
            cliphertext += chr(code)
        else:
            cliphertext += alp

    
    return plaintext

