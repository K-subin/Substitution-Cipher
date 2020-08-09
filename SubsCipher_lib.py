# Substitution Cipher 치환암호
import random
import os, sys

Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(key, msg):
    result = ""
    InSet = Alphabet
    OutSet = key

    for ch in msg:
        if ch.upper() in InSet:
            idx = InSet.find(ch.upper())
            if ch.isupper():
                result += OutSet[idx].upper()
            else:
                result += OutSet[idx].lower()
        else:
            result += ch
    return result

def decrypt(key, msg):
    result = ""
    InSet = key
    OutSet = Alphabet

    for ch in msg:
        if ch.upper() in InSet:
            idx = InSet.find(ch.upper())
            if ch.isupper():
                result += OutSet[idx].upper()
            else:
                result += OutSet[idx].lower()
        else:
            result += ch
    return result

# 키 유효성 검사 함수
def key_validation(key):
    if len(key) != len(Alphabet): # key 길이가 26이 아닐 때
        print("This key is invalid") # 오류
        return
    new_key = []
    for ch in key:
        if ch in new_key: # 똑같은 문자가 있을 때
            print("This key is invalid") # 오류
            return
        new_key.append(ch)
    print("This key is valid")

# 키 생성 함수
def key_generation():
    return "".join(random.sample(Alphabet, 26)) 
# Alphabet에서 랜덤으로 중복없이 26개를 가져온다.
# random.sample은 결과값으로 리스트를 반환하기때문에 join을 이용해 문자열로 변환
