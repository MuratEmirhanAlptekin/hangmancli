f = open("words.txt","r")
f2 = open("lesswords.txt","w")
letter = int(input("how many letters do you want?"))
letter+=1
for i in f:
    if len(i) == letter:
        f2.write(i)
