# Python 3.9.6

__author__ = 0xb301
__date__ = "2.3.22"
__description__ = "It seems so easy once you solve it _-_ In the end most of the functions were kind of useless?"

# Globals
imv: hex = 0xffffffff           #32bit

def main():
    pickles0 = [
        '9F', 'AE', '9C', 'B6', 
        'BD', 'B9', 'EF', 'EB', 
        'E6', '9E', 'B9', 'EC', 
        'B3', 'B9', 'E3', 'B9', 
        'BB', 'A8', '89', 'E3', 
        'BD', 'EF', 'BB', '96', 
        'B9', 'ED', 'E3', '89', 
        'B9', 'E4'
    ]
    pickles1 = [
        '9E', 'AD', '93', 'B5', 
        'BC', 'B8', 'EE', 'EA', 
        'E5', '90', 'BA', 'B8', 
        'EB', 'BA', 'ED', 'E3', 
        'E8', 'BC', 'EE', 'BA', 
        'ED', 'EB', 'B8', 'EE', 
        'EC', 'FB'
    ]
    pickles2 = [
        '9D', 'AC', '92', 'EB', 
        'B3', 'BF', 'ED', 'E9', 
        'E4', '97', 'B9', '94', 
        'E8', 'E1', 'B3', 'B9', 
        '94', 'BF', 'E3', 'E1', 
        'B7', 'BF', 'FF', 'FA'
    ]
    tea0(pickles0)
    tea1(pickles1) 
    tea2(pickles2)

# Solutions [only 1 & 2 are accessible I believe? since beerBeverage is either 1 or 2]
def tea0(secret: str) -> str:
    flag: str = ''
    original: list = []
    for i in secret:
        eax = hex((int('0x' + i, 16)) ^ 0xffffffcb)
        eax = int(hex(int(eax, 16) + imv + 1)[-2:], 16)
        if eax + 0x4e < 0x7e:
            eax += 0x4e + 0x11

        elif hex(eax - 0x5f & (2 ** 32 - 1))[-2:] == 0x20:
            eax -= 0x64 #0x70-0x11 

        eax -= 0x11
        original.append(eax)
        flag += chr(eax)
    print(flag)
    print(original)
    return flag        
    
def tea1(secret: str) -> str:
    flag: str = ''
    original: list = []
    for i in secret:
        eax = hex((int('0x' + i, 16)) ^ 0xffffffcb)
        eax = int(hex(int(eax, 16) + imv + 1)[-2:], 16)
        if eax + 0x4d < 0x7e:
            eax += 0x4d + 0x12

        elif hex(eax - 0x5f & (2 ** 32 - 1))[-2:] == 0x20:
            eax -= 0x5f #0x71-0x12 

        eax -= 0x12
        original.append(eax)
        flag += chr(eax)
    print(flag)
    print(original)
    return flag        

def tea2(secret: str) -> str:
    flag: str = ''
    original: list = []
    for i in secret:
        eax = hex((int('0x' + i, 16)) ^ 0xffffffcb)
        eax = int(hex(int(eax, 16) + imv + 1)[-2:], 16)
        if eax + 0x4c < 0x7e:
            eax += 0x4c + 0x13

        elif hex(eax - 0x5f & (2 ** 32 - 1))[-2:] == 0x20:
            eax -= 0x5f

        eax -= 0x13
        original.append(eax)
        flag += chr(eax)
    print(flag)
    print(original)
    return flag

# Logic
def logic(pt: str) -> str:
    msg: list = []
    for i in range(len(pt)):
        edx = ord(pt[i])
        eax += 0x13
        if eax > 0x7e:
            eax -= 0x4c
            eax ^= 0xffffffcb
            msg.append([pt[i], eax - imv - 1])

        edx += 0x72
        if "0x" + hex(eax & (2 ** 32 -1))[-2:] == 0x20:
            eax = edx

        eax ^= 0xffffffcb
        msg.append([pt[i] ,eax - imv - 1])
    

if __name__ == "__main__":
    main()
