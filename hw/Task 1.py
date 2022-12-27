with open('D:/Task1.txt', 'r') as myfile:
    insfile = open('D:/insfile.txt', 'r')
    content = myfile.readlines()
    f = ''.join(insfile)
    content.insert(34, f)
with open('D:/Task1.txt', 'w') as myfile:
    content = "".join(content)
    myfile.write(content)
