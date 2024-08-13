saldo = 100.00
def atualizar_saldo(saldo, dep):
    return saldo + dep
poupança = 10000

for i in range(1):
    # email = input("Digite seu emal:")
    # senha = input("Digite sua senha:")
    # if (email== "david" and senha == "1234"):
    #     print("Acesso liberado")
        opçao = input("1-saque 2-deposito 3-transferencia 4-saldo")
        match opçao:
            case "1":
                saque = input ("informe o saque")
                if (saque > saldo):
                    print("Liberado")
                else:
                    print("Bloqueado volte ao inicio")    
            case "2":
                dep = float(input("Informe o valor do depósito: "))
                saldo = atualizar_saldo(saldo, dep)
                print(f"Seu saldo final é: R${saldo:.2f}") 
            case "3": 
                transferencia = input ("informe o valor da transferencia:") 
                if (transferencia > saldo):
                    print("Liberado a tranferecia sera realizada")
                else:
                    print("Bloqueado volte ao inicio ou deposite dinheiro")
            case "4":
                conta = input("informe qual conta você deseja ver corrente(1) poupança(2)")
                if (conta == 1):
                    print(saldo)
                else:
                    print (poupança)  
                   
                        
                           
                    
                