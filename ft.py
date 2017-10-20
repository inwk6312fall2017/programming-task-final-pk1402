f1=open("Book1.txt","r")
read_file=f1.read()
words=read_file.split()
longest = 0
for word in read_file.split():
    if len(word) > longest:
        longest = len(word)
        longest_word = word
 
print( "The longest word is %s" % longest_word )

