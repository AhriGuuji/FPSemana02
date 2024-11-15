phrase=input()
phrase2=input()
phrase_set=set()
phrase2_set=set()
for i in phrase.split(" "):
    phrase_set.add(i)
for i in phrase2.split(" "):
    phrase2_set.add(i)
final_phrase= phrase_set.intersection(phrase2_set)
lista=[]
for i in final_phrase:
    lista.append(i)
print(" ".join(lista))