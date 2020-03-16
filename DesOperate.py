# -*- coding: UTF-8 -*-

from DESConstant import *
from DESUtil import *

class DesOperate():
    def __init__(self):
        self.__m_arrOutKey = []

    def encry(self, text, keytext):
        self.make_keys(key_text=keytext)
        # print(self.__m_arrOutKey)
        text_bits = get_bits(text)
        text_bits = add_pads_if_necessary(text_bits)

        result = ''
        for i in range(0, len(text_bits), 64):
            result += self.DES(text_bits, i, (i + 64))

        # print(result)

        hex_cipher = ''
        i = 0
        while i < len(result):
            temp = "%x" % int(result[i:i + 4], 2)
            hex_cipher += temp
            i = i + 4
        return hex_cipher

    def decry(self, cipher, key_text):
        self.make_keys(key_text)

        text_bits = []
        ciphertext = ''
        for i in cipher:
            # conversion of hex-decimal form to binary form
            tempstr = str(bin(int(i, 16)))[2:]
            dislen = 4 - len(tempstr)
            ciphertext += '0'*dislen
            ciphertext += tempstr
        # print(ciphertext)
        for i in ciphertext:
            text_bits.append(int(i))

        text_bits = add_pads_if_necessary(text_bits)
        self.__m_arrOutKey.reverse()
        bin_mess = ''
        for i in range(0, len(text_bits), 64):
            bin_mess += self.DES(text_bits, i, (i + 64))

        i = 0
        text_mess = ''
        while i < len(bin_mess):
            # print(bin_mess[i:i+8])
            text_mess += chr(int((bin_mess[i:i + 8]), 2))
            # text_mess += ('\\x%x' % int((bin_mess[i:i + 8]), 2))
            i = i + 8
        return text_mess

    def DES(self, text_bits, start, end):
        block = []
        for i in range(start, end):
            block.append(text_bits[i])

        block = self.apply_IP(block)
        # print('ip', block)

        left_block = block[0:32]
        right_block = block[32:64]

        left_block, right_block = self.iterate(left_block, right_block)
        # print(left_block)
        # print(right_block)

        block = []
        block.extend(right_block)
        block.extend(left_block)

        block = self.apply_FP(block)
        # print(block)

        cipher_block = ''
        for i in block:
            cipher_block += str(i)
        return cipher_block

    def apply_IP(self, block):
        r = []
        r.extend(block)
        for i in range(0, 64):
            r[i] = block[pc_first[i] - 1]
        return r

    def apply_FP(self, block):
        """final permutaion
        """
        r = []
        r.extend(block)
        for i in range(0, 64):
            r[i] = block[pc_last[i] - 1]
        return r

    def e_box(self, block):
        """exapansion permutation to expand 32 bit block into 48 bit block
           also called E-box
        """
        dummy = []
        for i in range(48):
            dummy.append(block[des_E[i] - 1])

        r = []
        for i in range(0, 48, 6):
            j = i + 6
            r.append(dummy[i:j])
        return r

    def s_box(self, block):
        """s-box function to reduce 48 bit block to 32 bit block
        """
        r = []
        for i in range(0, 8):
            temp = [str(item) for item in block[i]]
            temp = int(''.join(temp), 2)
            binary = to_binary(chr(des_S[i][temp]))
            r.extend(binary[4:8])
        return r

    def p_box(self, block):
        """p-box permutation
        """
        r = []
        r.extend(block)
        for i in range(32):
            r[i] = block[des_P[i] - 1]
        return r

    def iterate(self, left_block, right_block):
        """iterating  for the 16 rounds
        """
        for j in range(0, 16):
            d9 = []
            d9.extend(right_block)
            right_block = self.e_box(right_block)
            for i in range(0, 8):
                di = i * 6
                for k in range(0, 6):
                    right_block[i][k] ^= self.__m_arrOutKey[j][di + k]
            right_block = self.s_box(right_block)
            right_block = self.p_box(right_block)
            for i in range(0, 32):
                right_block[i] ^= left_block[i]

            left_block = []
            left_block.extend(d9)

        return left_block, right_block

    def make_keys(self, key_text):
        self.__m_arrOutKey = []
        key = []
        for i in key_text:
            key.extend(to_binary(i))
        C = []
        D = []
        for i in range(28):
            C.append(key[keyleft[i] - 1])
        for i in range(28):
            D.append(key[keyright[i] - 1])

        # print('before make key:', C, D)

        for i in range(0, 16):
            if lefttable[i] == 1:
                C = left_shift(C, 1)
                D = left_shift(D, 1)
            else:
                C = left_shift(C, 2)
                D = left_shift(D, 2)
            CD = []
            CD.extend(C)
            CD.extend(D)
            dummy = []
            for i in range(48):
                dummy.append(CD[keychoose[i] - 1])
            self.__m_arrOutKey.append(dummy)

if __name__ == '__main__':
    desop = DesOperate()
    string = 'Hello world!'
    result = desop.encry(string, 'aaaaaaaa')
    print(result)
    result = desop.decry(result, 'aaaaaaaa')
    print(result)
