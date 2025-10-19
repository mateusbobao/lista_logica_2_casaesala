N = float(input("Digite a nota: "))
inteiro = int(N)
resto = N-inteiro
if resto>0.5:
    print("Nota arredondada:",inteiro+1)
else:
    print("Nota arredondada:",inteiro)