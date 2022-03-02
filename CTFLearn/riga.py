# Python 3.9.6

__author__ = 0xb301
__date__ = "2.3.22"
__description__ = "It seems so easy once you solve it _-_"

# Globals
imv: hex = 0xffffffff           #32bit

def main():
    secret = [
        '9D', 'AC', '92', 'EB', 
        'B3', 'BF', 'ED', 'E9', 
        'E4', '97', 'B9', '94', 
        'E8', 'E1', 'B3', 'B9', 
        '94', 'BF', 'E3', 'E1', 
        'B7', 'BF', 'FF', 'FA'
    ]
    solution(secret) 
    return

# Solution
def solution(secret: str) -> str:
    flag: str = ''
    original: list = []
    for i in secret:
        eax = hex((int('0x'+i, 16)) ^ 0xffffffcb)
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
