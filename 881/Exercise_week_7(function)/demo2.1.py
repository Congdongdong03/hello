def truple(sentence):
    result=""
    for i in range(0,len(sentence)):
        result +=sentence[i]*3
        print(result)
    return result
sentence = input('Enter a sentence:')
finalresult = truple(sentence)
print('Triple effect:',finalresult)