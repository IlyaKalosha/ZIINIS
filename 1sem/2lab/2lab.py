#-*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import binascii

with open("input_binary.txt","w") as binar:
	binar.write(bin(int.from_bytes('Kalosha Ilya Valer\'evich'.encode(),'big')))

with open("input.txt") as f:
	a=np.array(list(f.read()))
b,cnt = np.unique(a, return_counts=True)
p=cnt/np.sum(cnt)
zip_iterator = zip(b,cnt)
value_dict = dict(zip_iterator)
plt.bar(list(value_dict.keys()),value_dict.values(),color='g')
plt.show()
First_H=-np.sum(p*np.log2(p))
print(b)
print(cnt)
print(First_H)

print("------------------------------------")

with open("input_binary.txt") as f:
	a=np.array(list(f.read()))
with open("input_binary.txt") as f:
	word_bit=f.read()	
a=list(a)
a.remove('b')
word=int(word_bit,2).to_bytes((int(word_bit,2).bit_length()+7)//8,'big').decode()
#print(word)
b,cnt = np.unique(a, return_counts=True)
p=cnt/np.sum(cnt)
zip_iterator = zip(b,cnt)
value_dict = dict(zip_iterator)
plt.bar(list(value_dict.keys()),value_dict.values(),color='g')
plt.show()
Sec_H=-np.sum(p*np.log2(p))
print(b)
print(cnt)
print(Sec_H)

#количество информации в Kalosha Ilya Valer'evich
s=list('Kalosha Ilya Valer\'evich')
len_s = len(s)
s_to_bin = bin(int.from_bytes('Kalosha Ilya Valer\'evich'.encode(),'big'))
len_bin_s=len(s_to_bin)
I_s=First_H*len_s
I_bin_s=Sec_H*len_bin_s
print("------------------------------------")
print(I_s)
print(I_bin_s)


p=0.1
p2=0.5
p3=1
print("------------------------------------")
print(I_s*(1-p))
print(I_bin_s*(1-p))
print("------------------------------------")
print(I_s*(1-p2))
print(I_bin_s*(1-p2))
print("------------------------------------")
print(I_s*(1-p3))
print(I_bin_s*(1-p3))
print("------------------------------------")
