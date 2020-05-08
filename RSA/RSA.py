import random
import math
from DES.DESUtil import *

class RSA:
    def __init__(self):
        self.prime_num_list = []
        self.generate_prime_num(100)
        self.calculate_PQN()
        self.calculate_eulerN()
        self.calculate_DE()

    def getEDN(self):
        return self.E, self.D, self.N


    def calculate_DE(self):
        for i in range(2, self.eulerN):
            flag = True
            for j in range(2, i + 1):
                if i % j == 0 and self.eulerN % j == 0:
                    flag = False
                    break
            if flag:
                self.E = i
                break

        self.D = 2
        while True:
            if (self.D * self.E - 1) % self.eulerN == 0:
                break
            self.D += 1

        # print("E:", self.E, "D:", self.D)
        return self.D, self.E


    def calculate_PQN(self):
        self.p = self.prime_num_list[random.randint(6, len(self.prime_num_list) - 1)]
        self.q = self.prime_num_list[random.randint(6, len(self.prime_num_list) - 1)]
        while self.q == self.p:
            self.q = self.prime_num_list[random.randint(0, len(self.prime_num_list) - 1)]
        self.N = self.p * self.q
        # print("p:", self.p, "q:", self.q, "N:", self.N)
        return self.p, self.q, self.N

    def calculate_eulerN(self):
        self.eulerN = self.euler(self.N)
        # print("Euluer N:", self.eulerN)

    def euler(self, N):
        res = N
        for i in range(2, math.ceil(N**0.5), 1):
            if N % i == 0:
                res = res - res/i
                N /= i
                while N % i == 0:
                    N /= i
        if N > 1:
            res = res - res/N
        return round(res)

    def generate_prime_num(self, maxNum):
        for i in range(2, maxNum):
            flag = True
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    flag = False
            if flag:
                self.prime_num_list.append(i)
        # print("prime_num_list：", self.prime_num_list)

def get_EDN():
    rsa = RSA()
    return rsa.getEDN()

def quick_mod(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans

def encodeRSA(text, E, N):
    result = ''
    for s in text:
        n = ord(s)
        en_num = quick_mod(n, E, N)
        result = result + str(en_num) + '_'
    return result[:-1]

def decodeRSA(text, D, N):
    result = ''
    slist = text.split('_')
    for s in slist:
        n = int(s)
        de_num = quick_mod(n, D, N)
        result = result + chr(de_num)
    return result


if __name__ == '__main__':
    E, D, N = get_EDN()
    password = encodeRSA("abcdefgh", E, N)
    print("password:", password)
    show = decodeRSA(password, D, N)
    print("show:", show)