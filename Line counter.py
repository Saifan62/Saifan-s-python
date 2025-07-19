file = open("Saifan's lifestyle.txt", 'r')
Counter = 0
Content= file.read()
Colist = Content.split('\n')
for i in Colist:
    if i:
        Counter += 1
print("This is the number of lines in the file:")
print(Counter)
file.close()