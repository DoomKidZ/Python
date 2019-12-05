num = int(input("\nint: "))
x = int(1)

def dec2bin(num):                       #Solicita que um valor inteiro seja informado

    b = ''                              #Declara a variavel 'b' como uma string vazia                          
    while num != 0:                     #Informa que haverá um loop enquanto o numero 'num' for diferente de 0
        b = b + str(num % 2)            #Diz que 'b' receberá a concatenação dos restos de divisão do numero 'num'
        num = int(num / 2)              #Dividirá 'num' por 2 para o próximo passo de conversão
    return b[::]                        #Retorna a lista de caracteres binarios, na ordem correta quando [::-1], na ordem contraria quando [::]

while (x == 1 ):
    if (num > 18446744073709551616):
        print("\nO valor digitado utrapassa 64 bits.")
        num = int(input("\nDigite novamente: "))
    else:
        bin = dec2bin(num)                      #Chamada de Função
        x=0

        print ("\n{\n    B"+bin[0:8]+",")       #Exibição da sequência binária que forma o número informado.
        print ("    B"+bin[8:16]+",")
        print ("    B"+bin[16:24]+",")
        print ("    B"+bin[24:32]+",")

        print ("    B"+bin[32:40]+",")
        print ("    B"+bin[40:48]+",")
        print ("    B"+bin[48:56]+",")
        print ("    B"+bin[56:64]+"\n}")



