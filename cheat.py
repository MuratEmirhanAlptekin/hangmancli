f = open("lesswords.txt","r")
for i in f:
    if i[1] == "o" and i[3] == "e":
        print(i) 
