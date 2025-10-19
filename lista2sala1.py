N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
media = (N1+N2+N3)/3
if media>=6:
    print("Aluno aprovado com media: ",media)
else:
    print("Aluno reprovado com media: ",media)
