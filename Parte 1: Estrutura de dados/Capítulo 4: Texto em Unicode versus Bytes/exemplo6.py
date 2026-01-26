# combinando unicode

s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2)


from unicodedata import normalize

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)
print(nfc_equal(s1, s2))