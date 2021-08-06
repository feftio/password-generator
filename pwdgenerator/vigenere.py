from __future__ import annotations
import typing as t
from pwdgenerator.utils import stuple, lower, slist


class Vigenere:
    def __init__(self, alphabet: str):
        self.alphabet: str = alphabet

    def __basecrypt(self, plaintext: str, key: str, bias: int) -> str:
        alphabet, result, islower, i = self.alphabet, [], False, 0
        plaintext = slist(plaintext)
        key = stuple(key)
        while(i != len(plaintext)):
            char = plaintext[i]
            islower = char.islower()
            kchar = key[i % len(key)]
            try:
                charindex = alphabet.index(char.lower())
                kcharindex = alphabet.index(kchar.lower())
            except ValueError:
                plaintext.pop(i)
                result.append(char)
                continue
            alpchar = alphabet[(charindex + (bias * kcharindex)) %
                               len(alphabet)]
            alpchar = alpchar if islower is True else alpchar.upper()
            result.append(alpchar)
            i += 1
        return ''.join(result)

    def decrypt(self, plaintext: str, key: str) -> str:
        return self.__basecrypt(plaintext, key, -1)

    def encrypt(self, plaintext: str, key: str) -> str:
        return self.__basecrypt(plaintext, key, 1)
