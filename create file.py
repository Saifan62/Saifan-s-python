new_file = open('Newfile.txt', 'x')
new_file.close()

import os
print("Checking if myfile.txt exists or not....")
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("myfile.txt deleted successfully")
else:
    print("myfile.txt does not exist")

my_file = open('myfile.txt', 'w')
my_file.write("Hi I am a penguin. I am a cute penguin.")
my_file.close()
os.remove("Codingal.txt")
print("Codingal.txt deleted successfully")
os.rmdir('Folder')
