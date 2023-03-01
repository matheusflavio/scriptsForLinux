import pyperclip

phrase = list(input("Digite o que quer que fique no FoRmAtO\n"))
for i in range(len(phrase)):
    if(i%2 == 0):
        phrase[i] = phrase[i].upper()   
    else:
        phrase[i] = phrase[i].lower()
phrase = "".join(phrase)
print(phrase)
pyperclip.copy(phrase)