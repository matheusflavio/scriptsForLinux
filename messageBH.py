import time, pyautogui, sys
import pandas as pd
import numpy as np

excel = pd.read_excel(r'%s' % sys.argv[1])
month = sys.argv[1][-7:-5]
rent, light, iptu, condominio, internet = excel.Valor[0+18], excel.Valor[1+18], excel.Valor[2+18], excel.Valor[3+18], excel.Valor[4+18]
months = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
total = rent + light + iptu + condominio

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
        time.sleep(1)
        writeAndEnter('WhatsApp')
        time.sleep(15)
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

def makeMessage(contato, mes, aluguel, luz, iptu, condominio, internet, total):
    searchContact(contato)
    writeAndEnter('Bom dia, tudo bem?')
    message = 'Sobre as contas do mes de ' + mes + ', ficou assim:\n'
    writeAndEnter(message)
    #sendFiles()
    #time.sleep(5)
    if(contact != contactsList[0]): #Minhas Coisas\Guilherme Ranier
        writeAndEnter(replaceDotToComma(str('%.2f' % resolve(aluguel))) + '(aluguel) + ' + replaceDotToComma(str('%.2f' % resolve(luz))) + '(luz) + ' + replaceDotToComma(str('%.2f' % resolve(iptu))) + '(iptu) + ' + replaceDotToComma(str('%.2f' % resolve(condominio))) + '(condominio) + ' + replaceDotToComma(str('%.2f' % resolve(internet))) + '(internet).\nTotal: ' + replaceDotToComma(str(resolve(total))) + ' / 3 + ' + replaceDotToComma(str(np.round(internet,2))) + '(internet)= ' + replaceDotToComma(str(np.round(total/3 + internet,2))))
    else:
        writeAndEnter(replaceDotToComma(str('%.2f' % resolve(aluguel))) + '(aluguel) + ' + replaceDotToComma(str('%.2f' % resolve(luz))) + '(luz) + ' + replaceDotToComma(str('%.2f' % resolve(iptu))) + '(iptu) + ' + replaceDotToComma(str('%.2f' % resolve(condominio))) + '(condominio) ' + replaceDotToComma(str('%.2f' % resolve(np.multiply(internet,-2)))) + '(internet).\nTotal: ' + replaceDotToComma(str(resolve(total))) + ' / 3 ' + replaceDotToComma(str('%.2f' % resolve(np.multiply(internet,-2)))) + '(internet) = ' + replaceDotToComma(str(resolve(np.round(total/3 - np.multiply(internet,2),2)))))
    if (contato != contactsList[1]): #Para Testes\Geraldo
        message2 = 'Favor enviar para essa conta:\nPIX: flavio.matheusgsilva@gmail.com (PICPAY)'
        writeAndEnter(message2)
        writeAndEnter('Qualquer problema ou duvida basta me perguntar, ok?')
    writeAndEnter('Esse mes a conta de luz vai demorar mais um pouco para chegar por causa das tretas que houveram antes. Ao olhar com a cemig, foi-me dito que a conta de marco provavelmente chega dia 06/03')
    pyautogui.hotkey("ctrl","v")
    pyautogui.press('enter')
    time.sleep(1)
    writeAndEnter("Assim que a conta de luz chegar eu mando mensagem novamente")
    

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
    makeMessage(contact, months[int(month)-1], rent, light, iptu, condominio, internet, total)