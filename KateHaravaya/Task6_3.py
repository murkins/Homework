'''Task6_3. Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc.
until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

<em> Encryption:
Keyword is "Crypto"

* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
</em>'''

import string
class Cipher:
    def __init__(self, key):
        self.key = key
        self.usual_to_encr = {}
        self.encr_to_usial = {}

        s_1 = list(string.ascii_uppercase)
        s_2 = list(key.upper())

        for i in s_1:
            if i not in s_2:
                s_2.append(i)

        for i in range(26):
            s1_up = s_1[i]
            s2_up = s_2[i]

            s1_low = s_1[i].lower()
            s2_low = s_2[i].lower()

            self.usual_to_encr[s1_up] = s2_up
            self.usual_to_encr[s1_low] = s2_low

            self.encr_to_usial[s2_up] = s1_up
            self.encr_to_usial[s2_low] = s1_low

    def encrypt(self, s):
        new_s = []
        for c in s:
            if c in self.usual_to_encr:
                new_s.append(self.usual_to_encr[c])
            else:
                new_s.append(c)
        return "".join(new_s)


    def decrypt(self, s):
        new_s = []
        for c in s:
            if c in self.encr_to_usial:
                new_s.append(self.encr_to_usial[c])
            else:
                new_s.append(c)
        return "".join(new_s)


k = Cipher("crypto")
print(k.encrypt("Hello world"))
print(k.decrypt("Fjedhc dn atidsn"))
