#6c. Writea  program to append text to a file and display entire text.

f=open('abc.txt','at')
f.write('\nPython file handlind is easy to learn\n')
f.close()
f=open('abc.txt','r')
st=f.read()
print(st)
f.close()
