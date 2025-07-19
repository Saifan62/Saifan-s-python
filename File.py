file = open("Codingal.txt")
print(file.read())
file.close()

file_read = open('Codingal.txt', 'r')
print("File opened in read mode:")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
print("File opened in write mode:")
file_write.write("Hi I am Saifan. I am a Python Developer.")
file_write.close()

file_append = open('Codingal.txt', 'a')
print("File opened in append mode:")
file_append.write(" I am 11 years old.")
file_append.close()
