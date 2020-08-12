ETAOIN =  'ETAOINSHRDLCUMWFGYPBVKJXQZ' # 빈도순서
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#--- 알파벳 빈도를 계산하는 함수
def getLetterCount(message):
    letterCount = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0,
                    'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 
                    'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 
                    'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    for char in message.upper():
        if char in LETTERS:
            letterCount[char] += 1
    
    return letterCount

#--- items = (key, value) = (items[0], items[1])
def getItemZero(items):
    return items[0]

#--- 알파벳의 빈도 순으로 문자열 만들기
def getFreqOrder(message):
    letter_freq_dic = getLetterCount(message) # dic = {'A' : 25, ...}
    
    # dic = {25 : ['A', 'I'], 7:['B','U']...} 
    # (key, value) = (freq, alphabet)
    freq_letter_dic = {}
    for char in LETTERS:
        if letter_freq_dic[char] not in freq_letter_dic: # 현재 알파벳의 빈도가 처음 나온 것
            freq_letter_dic[letter_freq_dic[char]] = [char] # 리스트
        else:
            freq_letter_dic[letter_freq_dic[char]].append(char) # 리스트에 추가
    
    # dic = {25 : 'AI', 7:'UB' ...} 
    for freq in freq_letter_dic:
        freq_letter_dic[freq].sort(key=ETAOIN.find, reverse=False) # 빈도수에 따라서 정렬, 오름차순
        freq_letter_dic[freq] = ''.join(freq_letter_dic[freq]) # 문자열로
    
    # 빈도 순서대로 정렬
    # [(44, 'E'), (38, 'T'), ...]
    freqPairs = list(freq_letter_dic.items())    
    freqPairs.sort(key=getItemZero, reverse=True) #내림차순 
    
    # dic = {'E' 'T' ...}
    freq_order_list = []
    for freq_pair in freqPairs:
        freq_order_list.append(freq_pair[1])

    # dic = 'ET...'
    return ''.join(freq_order_list)

#------
def Freq2Key(freq_order):
    temp_dic = {}

    # {'E':'C', 'T':'M', ...}
    i = 0
    for char in freq_order:
        temp_dic[ETAOIN[i]] = char
        i += 1

    # [('E', 'C'), ...]
    temp_list = list(temp_dic.items())

    # [('A', 'P'), ('B', 'O') ...] 알파벳순
    temp_list.sort(key=getItemZero) #오름차순

    #['P', 'O', ...]
    temp_key_list = []
    for item in temp_list:
        temp_key_list.append(item[1])

    return ''.join(temp_key_list)
