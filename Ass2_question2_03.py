def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def is_likely_english(text, common_words):
    words = text.split()
    return any(word.upper() in common_words for word in words)


ciphertext = "VZ FRY5VFU VZCNGVRAG NAQ N VVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG B5 PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG V5 LBH UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
common_words = {"THE", "AND", "OF", "TO", "A", "IN", "THAT", "IS", "I", "IT", "FOR", "WITH"}

for shift in range(1, 26):
    decrypted = decrypt(ciphertext, shift)
    if is_likely_english(decrypted, common_words):
        print(f"Shift {shift} : {decrypted}")