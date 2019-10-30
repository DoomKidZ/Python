resp = str(input("Iniciar teste? (sim/não) "))
print()

while (resp == 'sim'):
    Mbits = float(input("Digite a velocidade da sua internet (MB): "))
    MBytes = float(input("Digite o tamanho do arquivo (MB): "))

    Mbits = Mbits/8

    #Declaração da variável 'Tamanho'.
    Tamanho = float()
    Tamanho == 0

    #Declaração das variáveis 'min' e 'sec' como contadore dos minutos e segundos.
    sec = int()
    min = int()
    sec == 0

    #Espaço de separação.. UwU
    print()

    #Estrutura de repetição em que cada loop é considerado como 1 segundo até atingir 60 e contar o minuto.
    while ((Tamanho) < (MBytes*1.024)):
        Tamanho = Tamanho + Mbits 
        sec = sec + 1

        if (sec == 60):
            min = min + 1
            sec = 0

    #Exibição de resultado    
    print()
    print("O tempo aproximado de download é de",(min),"minutos e",(sec),"segundos.")
    print()
    resp = input("Testar de novo? (sim/não) ")