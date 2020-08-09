import os, sys

def ReadFile(in_file):
    if not os.path.exists(in_file): # 파일이 존재하지 않을 때
        print("file %s does not exist." %(in_file))
        sys.exit()
    InFileObj = open(in_file)
    file_content = InFileObj.read()
    InFileObj.close()

    return file_content

def WriteFile(out_file, message):
    if os.path.exists(out_file): # 이미 파일이 존재할 때
        print('This will overwrite the file %s. (C)ontinue or (Q)uit' %(out_file))
        response = input('--->')
        if not response.lower().startswith('c'):
            sys.exit()
    OutFileObj = open(out_file, 'w')
    OutFileObj.write(message)
    OutFileObj.close()

    return 0