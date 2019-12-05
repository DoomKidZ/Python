PesoPeixes = float(input("Digite o peso: "))

if (PesoPeixes > 50):
    print("O peso excedente é de:",PesoPeixes-50,"kg.")
    print("A multa à pagar por esse excedente é de: R$",4*(PesoPeixes-50))
else:
    print("Não há multa à pagar.")
    