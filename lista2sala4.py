A = int(input("Insira o primeiro lado do triangulo: "))
B = int(input("Insira o segundo lado do triangulo: "))
C = int(input("Insira o terceiro lado do triangulo: "))
if A<B+C and B<A+C and C<A+B:
    if A==B and B==C:
        print("Triangulo é equilátero")
    elif A==B or A==C or B==C:
        print("Triangulo é isósceles")
    else:
        print("Triangulo é escaleno")
else:
    print("Os valores nao formam um triangulo")