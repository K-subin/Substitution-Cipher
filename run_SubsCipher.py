import SubsCipher_lib
import File_IO_lib

# 키 생성
key = SubsCipher_lib.key_generation()
print('[key]', key, '\n')

# 평문 txt 파일 불러오기
my_text = File_IO_lib.ReadFile('치환암호/my_text.txt')
print('[message]')
print(my_text,'\n')

# 암호문 생성
my_cipher = SubsCipher_lib.encrypt(key, my_text)
print('[Cipher message]')
print(my_cipher,'\n')

# 암호문 txt 파일 저장하기
File_IO_lib.WriteFile('치환암호/my_cipher.txt', my_cipher)

# 복호문 생성
my_recovered = SubsCipher_lib.decrypt(key, my_cipher)
print('[Recovered message]')
print(my_recovered,'\n')

# 암호문 txt 파일 저장하기
File_IO_lib.WriteFile('치환암호/my_recovered.txt', my_recovered)