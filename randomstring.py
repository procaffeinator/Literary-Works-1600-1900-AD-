from random import choice
from string import ascii_uppercase

file_object=open("random_string.txt","a")
file_object.write(''.join(choice(ascii_uppercase) for i in range(10000)))
file_object.close()



