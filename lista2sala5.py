A = int(input("Digite o primeiro numero: "))
B = int(input("Digite o segundo numero: "))
C = int(input("Digite o terceiro numero: "))
if A<B and A<C:
    if B<C:
        print("Numeros em ordem crescente: ",A,B,C)
    else:
        print("Numeros em ordem crescente: ",A,C,B)
if B<A and B<C:
    if A<C:
        print("Numeros em ordem crescente: ",B,A,C)
    else:
        print("Numeros em ordem crescente: ",B,C,A)
if C<A and C<B:
    if B<A:
        print("Numeros em ordem crescente: ",C,B,A)
    else:
        print("Numeros em ordem crescente: ",C,A,B)