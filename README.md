# Substitution-Cipher
- 치환암호 암호화, 복호화 라이브러리 구현
- 치환암호 실행 코드 구현
- 암호문 빈도분석 코드 구현
- 빈도분석 공격을 이용하여 치환암호 해독 구현

## 치환암호 구조

![img](https://user-images.githubusercontent.com/68969252/89994930-c2040c00-dcc3-11ea-99cd-d8da326f7fed.png)

치환암호의 키 값은 위 그림과 같이 치환표이며 송신자와 수신자는 치환표를 공유

## 치환암호 공격방법
치환암호 키 공간 = 26 x 25 x 24 x ... x 1
- 전사공격으로 사실상 해독 불가능

치환암호 취약점
- 평문에 등장하는 문자의 빈도가 암호문으로 변환된 뒤에도 암호문 내에서 동일한 빈도로 나타남
- 빈도분석 공격으로 치환암호 해독 가능

## 실행화면

### run_SubsCipher.py 실행

![치1](https://user-images.githubusercontent.com/68969252/89994382-02af5580-dcc3-11ea-9780-d96f99e5d23f.PNG)

### break_SubsCipher.py 실행

![치3](https://user-images.githubusercontent.com/68969252/89994529-34282100-dcc3-11ea-9007-bdbe335ab6cc.PNG)

- 정확한 해독 불가능
- 글이 길수록 정확도 올라감
- 이후에 특정 문맥에 필요한 문법 유추 또는 같은 문자 반복 유추 등을 통해 정확한 평문 구할 수 있음
