print('''

          ****************
          ***   MENU   ***
          ****************
''')
saldo =  0
limite = 500
extrato = ''
numeros_de_saques = 0
LIMITES_SAQUES = 3


opçao = -1

while opçao !="0":      #realiza a seleção das opcões
    opçao = int(input('[1]Depositar\n[2]Sacar\n[3]Extrato\n[4]Sair\n:'))  
    
    if opçao == 1:   #realiza depositos
         deposito = float(input('Informe o valor do deposito:')) 
         if deposito > 0:
            saldo +=  deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            
         else:
              print('Operação falhou! O valor informado é invalido!')
#numero_operacao += 1  
    elif opçao == 2:          #realiza saques
        saque = float(input('Informe o valor que deseja sacar:')) 
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numeros_de_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print('Operação falhou! voce nao tem saldo suficiente')
        elif excedeu_limite:
           print('Operação falhou!! O valor do saque excede o limite')
        elif excedeu_saques:
           print('Operação falhou!!! Número máximo de saque excedidos')
        elif saque > 0:
             saldo -= saque
             extrato += f'saque: R${saque:.2f}\n'
             numeros_de_saques += 1
        else:
            print('O valor informado é invalido')
           
    elif opçao == 3:            #exibe extratos
        print("\n###########EXTRATO##############")
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\n Saldo R$:{saldo:.2f}')
        print('##################################')
    elif opçao == 4:     #sair do programa
        break
    else:
        print('Por favor selecione novamente a opção desejada')


    

