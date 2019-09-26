import random

def op1(p, s):
    return sum([i * j for i, j in zip(s, p)]) % 256

def op2(m, k):
    return bytes([i ^ j for i, j in zip(m, k)])

def rop3(m, p):
    ret = b""
    for i in range(16):
        for j in range(16):
            if i == p[j]:
                ret += bytes([m[j]])
    return ret

def rop4(m, s):
    ret = b""
    for i in range(16):
        for j in range(256):
            if m[i] == s[j]:
                ret += bytes([j])
    return ret

'''
Linear Feedback Shift Register
'''
def stage0(m):
    random.seed('oalieno')
    p = [int(random.random() * 256) for i in range(16)]
    s = [int(random.random() * 256) for i in range(16)]
    c = b''
    for x in m:
        k = op1(p, s)
        c += bytes([x ^ k])
        s = s[1:] + [k]
    return c

'''
Substitution Permutation Network
'''
def stage1(m):
    random.seed('oalieno')
    k = [int(random.random() * 256) for i in range(16)]
    p = [i for i in range(16)]
    random.shuffle(p)
    s = [i for i in range(256)]
    random.shuffle(s)

    c = m
    for i in range(16):
        c = rop4(c, s)
        c = rop3(c, p)
        c = op2(c, k)
    return c

def decrypt(m):
    stage = [stage0, stage1]

    n = m
    for key in range(256):
        m = n
        for i in range(8):
            if (key & (1 << i)):
                m = stage[0](m)
            else:
                m = stage[1](m)
        print(m)

if __name__ == '__main__':
    cipher = open('cipher', 'rb').read()
    decrypt(cipher)
