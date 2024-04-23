def triple(sentence):
    return ''.join([char*3 for char in sentence])
result = triple('apple')
print(result)
if(result == 'aaappp'):
    print('correct')
else:
    print('Incorrect')

strings = ['apple']
result = [string * 3 for string in strings]
print(result)
