def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    cliphertext = ''
    for alp, number in enumerate(plaintext):
        if (alp >= 'a') and (alp <= 'z') or (alp >= 'A') and (alp <= 'Z'):
            delta = ord(key[number % len(key)])
            delta -= ord('a') if 'a' <= alp <= 'z' else ord('A')
            code = ord(alp) + delta
            if 'a' <= alp <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= alp <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += alp
    return ciphertext
                            


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    ciphertext = ''
    for alp, number in enumerate(plaintext):
        if (alp >= 'a') and (alp <= 'z') or (alp >= 'A') and (alp <= 'Z'):
            delta = ord(key[number % len(key)])
            delta -= ord('a') if 'a' <= alp <= 'z' else ord('A')
            code = ord(alp) - delta
            if 'a' <= alp <= 'z' and code > ord('z'):
                code += 26
            elif 'A' <= alp <= 'Z' and code > ord('Z'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += alp
    return plaintext
