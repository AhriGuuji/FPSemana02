phrase=input()
phrase=phrase.replace(" ","")
dicionary={}
for i in phrase:
    if i not in dicionary:
        dicionary[i] = phrase.count(i)
print(dicionary)