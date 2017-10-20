#f1=open("Book1.txt","r")
#read_file=f1.read()
#words=read_file.split()
#longest = 0
#for word in read_file.split():
    #if len(word) > longest:
        #longest = len(word)
        #longest_word = word
 
#print( "The longest word is %s" % longest_word )
f1 = open('Book1.txt','r')
read_file= f1.readlines()
string = read_file[0]
stringsplit = string.split()
d = []
for i in stringsplit:
    d.append(len(i))
    e = max(d)
for j in stringsplit:
    if len(j) == e:
        print("The longest word is", j)


