import os
import sys
import keyboard
import pyperclip
import pyautogui as pg
import threading
import time





num = 0
nome = ''
listas = ('ssimSSIMyyesYESY')
listan = ('nnãonaoN')

#os.system('cls') or None
def comecar():
    os.system('cls') or None
    print("""Digite "sair" para encerrar o programa                                      Gerador de scripts.
                                                                  Sugestões de Melhorias nas descrições de chamados
                        
     Informe o tipo de script que deseja gerar.
    1 = Tentativa de contato
    2 = Encerramento após 3 tentativas
          
    """)

    tiposcript = str(input('  '))
    os.system('cls') or None
    return analise_script(tiposcript)
    
def analise_script(tiposc):
    
    if tiposc == '1':
        return tentativa()
       
    elif tiposc == '2':
        return encerramento3()

    elif tiposc == 'sair':
        return sys.exit("Encerrando ...........")
    
    else:
        print(' A sua descrição não condiz com nenhum script geravel por esse código.')
        print(' Por favor tente novamente.')
        time.sleep(1)
        os.system('cls') or None
        return comecar()

def tentativa():
    
    num = pyperclip.paste()
    
    pyperclip.copy(f"""Registrar comentário: Tentativa de contato com solicitante através do telefone: {num} que foi informado no chamado. A ligação chamou até cair/caiu na caixa postal.

Caso tenha outro número de telefone fixo/celular para entrarmos em contato, favor informar.""")
    
    return comecar()

def encerramento3():
    numero = str(input(' Número do chamado:'))
    email = str(input(' E-mail do cliente:'))
    num = str(input(' numero do cliente:'))
    os.system('cls') or None
    texto = (f"""Prezado cliente,
O chamado/ticket {numero} está sendo encerrado por falta de contato, após 3 
tentativas por telefone {num}, e 3 notificações enviados ao e-mail {email}, para atendermos ao seu chamado/ticket.
Sendo assim, havendo o interesse deverá abrir um novo chamado/ticket, renovando-se todos os prazos de atendimento.
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

def acao_eventoCallback():
    global num, nome

     #Salva o numero
    pg.hotkey('ctrl', 'c')
    num = pyperclip.paste()

    #Entra em atividades em atualizar status
    pg.hotkey('alt', 't')
    pg.press('down')
    pg.press('up')
    pg.press('enter')
    #aperta windows + V
    pg.hotkey('winleft', 'v')
    #espera o click
    time.sleep(1)
    
      
    
    #coloca fechado no status
    for i in range(2): pg.press('up')
    
    #Cola o codigo na descrição do usuario
    for i in range(5): pg.press('tab')
    
    #salva nome
    nome = pyperclip.paste() 
    pyperclip.copy(f"""CALLBACK REALIZADO COM SUCESSO. Telefone de Contato: {num}. 

    Prezado(a), {nome} 

    Agradecemos por permitir-nos atender às suas necessidades com sucesso. Sua opinião é extremamente valiosa para nós, pois nos ajuda a melhorar continuamente nossos serviços e a qualidade do atendimento. 

    Em breve, você receberá um SMS ou e-mail contendo nossa pesquisa de satisfação. Por favor, reserve um momento para nos fornecer seu feedback. Desde já, agradecemos pela sua colaboração! 

    Atenciosamente.""")
    pg.hotkey('ctrl', 'v')
    
    evento_notificaCallback()


def acao_repete():
    global num, nome  
    time.sleep(1)
    #Entra em atividades em atualizar status
    pg.hotkey('alt', 't')
    pg.press('down')
    pg.press('up')
    pg.press('enter')
    time.sleep(1)
    
    #coloca fechado no status
    for i in range(2): pg.press('up')
    
    #Cola o codigo na descrição do usuario
    for i in range(5): pg.press('tab')
    
    pyperclip.copy(f"""CALLBACK REALIZADO COM SUCESSO. Telefone de Contato: {num}. 

    Prezado(a), {nome} 

    Agradecemos por permitir-nos atender às suas necessidades com sucesso. Sua opinião é extremamente valiosa para nós, pois nos ajuda a melhorar continuamente nossos serviços e a qualidade do atendimento. 

    Em breve, você receberá um SMS ou e-mail contendo nossa pesquisa de satisfação. Por favor, reserve um momento para nos fornecer seu feedback. Desde já, agradecemos pela sua colaboração! 

    Atenciosamente. """)
    pg.hotkey('ctrl', 'v')
    evento_RepeteCallback()
    
    
    #pergunta se existe outro chamado para mesma pessoa
def evento_notificaCallback():
    teclas_combinacao = ['ctrl', '1']
    while True:
        # Verificar se todas as teclas da combinação estão pressionadas
        if all(keyboard.is_pressed(tecla) for tecla in teclas_combinacao):
            acao_eventoCallback()  # Executar a ação desejada
            keyboard.wait(teclas_combinacao[0])
            
def evento_RepeteCallback():
    teclas_combinacao = ['ctrl', '2']
    while True:
        # Verificar se todas as teclas da combinação estão pressionadas
        if all(keyboard.is_pressed(tecla) for tecla in teclas_combinacao):
            acao_repete()  # Executar a ação desejada
            keyboard.wait(teclas_combinacao[0])



if __name__ == '__main__':
    thread_monitoramento2 = threading.Thread(target=evento_notificaCallback)
    thread_monitoramento2.daemon = True  # Isso permite que a thread seja encerrada quando o programa principal encerrar
    thread_monitoramento2.start()
    thread_monitoramento2 = threading.Thread(target=evento_RepeteCallback)
    thread_monitoramento2.daemon = True  # Isso permite que a thread seja encerrada quando o programa principal encerrar
    thread_monitoramento2.start()
    comecar()