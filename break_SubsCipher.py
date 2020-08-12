import SubsCipher_lib
import Freq_Order_lib
import File_IO_lib

ETAOIN =  'ETAOINSHRDLCUMWFGYPBVKJXQZ' # 빈도순서
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#---- 평문 txt 파일 가져오기
text = File_IO_lib.ReadFile('치환암호/my_text.txt')
print('<my message>\n', text)

#---- 암호문 txt 파일 가져오기
cipher_text = File_IO_lib.ReadFile('치환암호/my_cipher.txt')
print('<cipher message>\n', cipher_text)

#---- 암호문 txt 파일 알파벳 빈도 순서 구하기
freq_order = Freq_Order_lib.getFreqOrder(text)
print('\n<ETAOIN vs Freq order>')
print('ETAOIN     =', ETAOIN)
print('Freq order =', freq_order)

#---- 키 추측하기
key_guess = Freq_Order_lib.Freq2Key(freq_order)
print('\n<key_guess>\n',key_guess)

#---- 추측한 키로 암호문을 복호화해서 평문 추측하기
recovered_text = SubsCipher_lib.decrypt(key_guess, text)
print('\n<recovered message guess>\n', recovered_text)
