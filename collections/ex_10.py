#Napisz program zliczajacy liczbe wystapien kazdego znaku w podanym przez uzytkownika napisie. (użyj słownika)

string = "klapaucius"
dic = {}

for s in string:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

print(dic)