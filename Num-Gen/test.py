import string
import random
letters = 'abcde'
numbers = '12345'
count = 0
newstr = ''
while count < 5:
    newstr += letters[count]+numbers[count]
    count+=1

print(newstr)