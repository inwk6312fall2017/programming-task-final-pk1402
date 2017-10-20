f1 = open('Book3.txt','r')
read_file= f1.readlines()
string = read_file[0]
stringsplit = string.split()
d = []
for i in stringsplit:
    d.append(len(i))
    e = max(d)
for j in stringsplit:
    if len(j) == e:
        print("The longest word of book3 is", j)



