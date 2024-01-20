import os
import sys
import keyboard
import pyperclip
import pyautogui as pg
import threading
import time
import banco






listas = ('ssimSSIMyyesYESY')
listan = ('nnãonaoN')

#os.system('cls') or None
def comecar():
    os.system('cls') or None
    print("""Digite "sair" para encerrar o programa                                      Gerador de scripts.
                                                                  Sugestões de Melhorias nas descrições de chamados
                        
     Informe o tipo de script que deseja gerar.
    1 = CALLBACK
    2 = Adicionar 0
    3 = Tentativa de contato
    4 = Encerramento após 3 tentativas
          
    5 = Banco config""")

    tiposcript = str(input('  '))
    os.system('cls') or None
    return analise_script(tiposcript)
    
def analise_script(tiposc):
    
    if tiposc == '1':
        return solucao()
    
    elif tiposc == '2':
        numero = str(input(' Número de contato:'))
        os.system('cls') or None
        texto = (f'0{numero}')
        print(texto)
        colar(texto)
        return comecar()

    elif tiposc == '3':
        return tentativa()
       
    elif tiposc == '4':
        return encerramento3()


    elif tiposc == '5':
        banco.configb()
        return comecar()

    elif tiposc == 'sair':
        return sys.exit("Encerrando ...........")
    
    else:
        print(' A sua descrição não condiz com nenhum script geravel por esse código.')
        print(' Por favor tente novamente.')
        time.sleep(1)
        os.system('cls') or None
        return comecar()

def solucao():
    print(' Digite "voltar" para retornar à primeira página.\n')
    
    pessoa = str(input(' Nome do cliente:'))
    numero = str(input(' Número de contato:'))
    genero = banco.iniciarbc(pessoa)
    genp = gen(pessoa, genero)  # Passando o gênero para a função gen
    os.system('cls') or None
    texto = (f"""CALLBACK REALIZADO COM SUCESSO. 
Em contato por telefone ({numero}) com {genp} validou a solução do chamado. Sendo assim, autorizou o encerramento do chamado.
Prezado(a), Sua opinião nos ajudará a melhorar ainda mais nossos serviços e qualidade no atendimento, portanto será enviado um SMS/E-mail com nossa pesquisa de satisfação para que avalie, desde já agradecemos!""")
    print(texto)
    colar(texto)
    return comecar()


def tentativa():
    numero = str(input(' Número de contato:'))
    os.system('cls') or None
    texto = (f"""Tentativa de contato com solicitante através do telefone: {numero} que foi informado no chamado. A ligação chamou até cair/caiu na caixa postal.""")
    print(texto)
    colar(texto)
    input(' \nVoltar ao começo')
    os.system('cls') or None
    return comecar()

def encerramento3():
    numero = str(input(' Número do chamado:'))
    email = str(input(' E-mail do cliente:'))
    os.system('cls') or None
    texto = (f"""Prezado cliente,
O chamado/ticket {numero} está sendo encerrado por falta de contato, após 3 
tentativas por telefone e 3 notific02
ações enviados ao e-mail {email} para atendermos 
ao seu chamado/ticket.
Sendo assim, havendo o interesse deverá abrir um novo chamado/ticket, renovando-se todos 
os prazos de atendimento.
Caso o problema persista abra um novo chamado/ticket.
Atenciosamente.
Central de atendimento CTI- 3617-3900.""")
    print(texto)
    colar(texto)
    input(' \nVoltar ao começo')
    os.system('cls') or None
    return comecar()




def colar(texto):
    pyperclip.copy(texto)
    pg.click()

    
    keyboard.wait("enter")

    
    pg.hotkey("ctrl", "v")
    pg.press('enter')
    
    return comecar()


def gen(pessoa, genero):
    pessoa = pessoa.capitalize()
    if genero == 'f':
        return f'a senhora {pessoa}, a mesma'
    else:
        return f'o senhor {pessoa}, o mesmo'

def acao_eventoCallback():
    #Salva o numero
    pg.hotkey('ctrl', 'c')
    num = pyperclip.paste()
    #salva nome
    pg.hotkey('winleft', 'v')
    time.sleep(3)
    nome = pyperclip.paste()
    
    
    pyperclip.copy(f"""CALLBACK REALIZADO COM SUCESSO. 
Em contato por telefone ({num}) com o/a Sr/Sra. {nome} o mesmo validou a solução do chamado. Sendo assim, autorizou o encerramento do chamado.
Prezado(a), Sua opinião nos ajudará a melhorar ainda mais nossos serviços e qualidade no atendimento, portanto será enviado um SMS/E-mail com nossa pesquisa de satisfação para que avalie, desde já agradecemos!""")    
    
    
    #Entra em atividades em atualizar status
    pg.hotkey('alt', 't')
    pg.press('down')
    pg.press('up')
    pg.press('enter')
    time.sleep(2)
    
    #coloca fechado no status
    for i in range(2): pg.press('up')
    
    #Cola o codigo na descrição do usuario
    for i in range(5): pg.press('tab')
    pg.hotkey('ctrl', 'v')
    
    evento_RepeteCallback(num,nome)


def acao_repete(num,nome):    
    pyperclip.copy(f"""CALLBACK REALIZADO COM SUCESSO. 
    Em contato por telefone ({num}) com o/a Sr/Sra. {nome} o mesmo validou a solução do chamado.
    Sendo assim, autorizou o encerramento do chamado.
    Prezado(a),
    Sua opinião nos ajudará a melhorar ainda mais nossos serviços e qualidade no atendimento, portanto será enviado um SMS/E-mail com nossa pesquisa de satisfação para que avalie, desde já agradecemos!""")
    time.sleep(1)
    #Entra em atividades em atualizar status
    pg.hotkey('alt', 't')
    pg.press('down')
    pg.press('up')
    pg.press('enter')
    time.sleep(2)
    
    #coloca fechado no status
    for i in range(2): pg.press('up')
    
    #Cola o codigo na descrição do usuario
    for i in range(5): pg.press('tab')
    pg.hotkey('ctrl', 'v')
    evento_notificaCallback()
    
    
    #pergunta se existe outro chamado para mesma pessoa
def evento_notificaCallback():
    teclas_combinacao = ['ctrl', '1']
    while True:
        # Verificar se todas as teclas da combinação estão pressionadas
        if all(keyboard.is_pressed(tecla) for tecla in teclas_combinacao):
            acao_eventoCallback()  # Executar a ação desejada
            keyboard.wait(teclas_combinacao[0])
            
def evento_RepeteCallback(num,nome):
    teclas_combinacao = ['ctrl', '2']
    while True:
        # Verificar se todas as teclas da combinação estão pressionadas
        if all(keyboard.is_pressed(tecla) for tecla in teclas_combinacao):
            acao_repete(num,nome)  # Executar a ação desejada
            keyboard.wait(teclas_combinacao[0])



if __name__ == '__main__':
    thread_monitoramento2 = threading.Thread(target=evento_notificaCallback)
    thread_monitoramento2.daemon = True  # Isso permite que a thread seja encerrada quando o programa principal encerrar
    thread_monitoramento2.start()
    thread_monitoramento2 = threading.Thread(target=evento_RepeteCallback)
    thread_monitoramento2.daemon = True  # Isso permite que a thread seja encerrada quando o programa principal encerrar
    thread_monitoramento2.start()
    comecar()