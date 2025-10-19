A=float(input("Digite valor A: "))
if A>0:
    B=float(input("Digite valor B: "))
    C=float(input("Digite valor C: "))
    X1=(-B+(B*B-4*A*C))/2*A
    X2=(-B-(B*B-4*A*C))/2*A
    if X1==X2:   
        print("O valor que satisfaz a equação de segundo grau é: ",X1)
    else:
        print("Os valores que satisfazem a equação de segundo grau são: ",X1,X2)
else:
    print("Não é possível calcular uma equação de segundo grau sendo A < 0")