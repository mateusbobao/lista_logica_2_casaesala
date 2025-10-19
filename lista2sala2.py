N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
media = (N1+N2)/2
if media >=6:
    print("Aluno aprovado com media: ",media)
else:
    exame=float(input("Digite a nota de exame: "))
    media=(exame+media)/2
if media>=6:
    print("Aluno aprovado com nota de exame: ",exame,"e media: ",media)
else:
    print("Aluno reprovado com nota de exame: ",exame,"e media: ",media)
