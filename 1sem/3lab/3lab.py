import base64
import numpy as np
import matplotlib.pyplot as plt

def ShenonAndHartly(path):
	with open(path) as f:
		a=np.array(list(f.read()))
	b,cnt = np.unique(a, return_counts=True)
	p=cnt/np.sum(cnt)
	zip_iterator = zip(b,cnt)
	value_dict = dict(zip_iterator)
	plt.bar(list(value_dict.keys()),value_dict.values(),color='g')
	plt.show()
	First_H=-np.sum(p*np.log2(p))#shenon
	Second_H=np.log2(len(b))#hartly
	overfill=(Second_H - First_H/Second_H)*100
	print(b)
	print(cnt)
	print("Энтропия Шеннона: ",First_H)
	print("Энтропия Хартли: ",Second_H)
	print("Избыточность: ", overfill)


def XOR(a,b):
	a=list(a)
	b=list(b)
	if(len(a)>len(b)):
		for i in range(len(a)-len(b)):
			b.append(0)
	if(len(b)>len(a)):
		for i in range(len(b)-len(a)):
			a.append(0)
	#result=np.logical_xor(a,b)
	result=set(b)^set(a)
	return result

with open("input.txt") as f:
	input_string=f.read()

string_bytes=input_string.encode('ascii')
base64_bytes=base64.b64encode(string_bytes)
base64_string = base64_bytes.decode('ascii')

with open("output.txt","w") as output:
	output.write(base64_string)


print("Начальная строка: ",input_string)
print("Итоговая строка: ", base64_string)

print()
print()
print()
ShenonAndHartly("input.txt")
print()
print()
print()
ShenonAndHartly("output.txt")
print()
print()
print()
a="1298452313132"
b="67890051224"
a_ascii=a.encode('ascii')
a_base64=base64.b64encode(a_ascii)
b_ascii=b.encode('ascii')
b_base64=base64.b64encode(b_ascii)
res=XOR(a_ascii,b_ascii)
print(res)
print()
print()
print()
res=XOR(a_base64,b_base64)
print(res)


