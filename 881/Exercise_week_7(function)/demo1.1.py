def triple(sentence):
    return ''.join([char*3 for char in sentence])
reslut = triple('ap')
print(reslut)
if reslut=='aaappp':
    print('R')
else:
    print('W')