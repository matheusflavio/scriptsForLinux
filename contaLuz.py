import time, pyautogui, sys
import pandas as pd
import numpy as np

excel = pd.read_excel(r'%s' % sys.argv[1])
month = sys.argv[1][-7:-5]
light = excel.Valor[1+18]
months = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

ans = input("Eh um teste? (s/n): ")
if(ans == 's'):
    contactsList = ['Minhas Coisas', 'Para Testes']
if(ans == 'n'):
    contactsList = ['Guilherme Ranier', 'Geraldo', 'Relampago Marquinhos']

def writeAndEnter(text):
    pyautogui.write(text)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)

def openWpp(ans):
    if(ans == 'n'):
        pyautogui.click(5,5)
        time.sleep(0.3)
        writeAndEnter('WhatsApp')
        time.sleep(10)
        return "a"
    if(ans == 's'):
        pyautogui.hotkey('alt','tab')
        time.sleep(1)
    else:
        ans = input("O WhatsApp está aberto? (s/n): ")
        openWpp(ans)
ans = ''
openWpp(ans)


def replaceCommaToDot(text):
    return text.replace(',','.')

def replaceDotToComma(text):
    return text.replace('.',',')

def callWhatsApp():
    pyautogui.hotkey('alt','tab')
    time.sleep(0.2)

def searchContact(contact):
    #pyautogui.hotkey('ctrl','alt','/')
    pyautogui.click(165,140)
    time.sleep(0.3)
    pyautogui.write(contact)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.5)

def resolve(a):
    return np.round(np.ceil(100 * a))/100

def makeMessage(contato, mes, luz):
    searchContact(contato)
    writeAndEnter('Bom dia, tudo bem?')
    writeAndEnter('Sobre a conta de Luz do mes de ' + mes + ', ficou assim:\n')
    writeAndEnter('Luz (total): ' + replaceDotToComma(str('%.2f' % resolve(luz))) + '.\n' + replaceDotToComma(str(resolve(luz))) + ' / 3 = ' + replaceDotToComma(str('%.2f' % resolve(luz/3)))+ ' para cada um' )
    if (contato != contactsList[1]): #Para Testes\Geraldo
        message2 = 'Favor enviar para essa conta:\nPIX: flavio.matheusgsilva@gmail.com (PICPAY)'
        writeAndEnter(message2)
        writeAndEnter('Qualquer problema ou duvida basta me perguntar, ok?')    

def sendFiles():
    pyautogui.click(480,710)
    time.sleep(0.3)
    pyautogui.click(485,445)
    time.sleep(0.5)
    pyautogui.click(800,600)
    writeAndEnter('documents')
    writeAndEnter('pessoal')
    writeAndEnter('apto')
    writeAndEnter(monthYear)
    writeAndEnter('contas')
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('enter',presses=8, interval=0.5)

#callWhatsApp()

for contact in contactsList:
    makeMessage(contact, months[int(month)-1], light)