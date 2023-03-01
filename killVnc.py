import os

for number in range(100001):
    myString = ("vncserver -kill :"+ str(number))
    os.system(myString)