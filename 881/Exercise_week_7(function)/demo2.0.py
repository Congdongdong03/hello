def triple(sentance):
    result=""
    for i in range(0,len(sentance)):
        letter = sentance[i]
        result += letter * 3
        print(result)
    return result
sentance=input('Enter a sentence:')
triple_result = triple(sentance)
print('Triple effect:',triple_result )