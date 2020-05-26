def messageFromBinaryCode(code):
    res = ''
    stuff = [code[i:i+8] for i in range(0,len(code),8)]
    for i in stuff:
        res += chr(int(eval('0b'+i)))
    return res
