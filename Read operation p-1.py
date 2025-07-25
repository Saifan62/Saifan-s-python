file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
file.write("Hi, I am a penguin. I love to swim.")
file.close()

file = open('Codingal.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("\n Read the fifth line \n")
lines = file.readlines()
print(lines[4]) 
file.close()
 

