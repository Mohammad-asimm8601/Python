with open("myfile.txt", 'w') as file:
    file.write('Hello World\nThis is the second line\nThis is he third line')
  
myfile = open('myfile.txt')
txt = myfile.read()
print(txt)


myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readlines())

myfile.close()


with open('myfile.txt', 'a') as file:
    file.write("\nI am here")

content = open('myfile.txt')
print(content.read())