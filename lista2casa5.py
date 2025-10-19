bruto = float(input("Insira o salario bruto: "))
hrtrab = int(input("Insira as horas trabalhadas: "))
if bruto<800:
    liquido=bruto
    if hrtrab>160:
        adicional=(bruto/160)*(50/100)*(hrtrab-160)
        print("Salario liquido de:",liquido,"com adicional de:",adicional)
    else:
        print("Salario liquido de:",liquido)
elif bruto >=800 and bruto <=1600:
    liquido=bruto-(bruto*(8/100))-(bruto*(5/100))
    if hrtrab>160:
        adicional=(bruto/160)*(50/100)*(hrtrab-160)
        print("Salario liquido de:",liquido,"com adicional de:",adicional)
    else:
        print("Salario liquido de:",liquido)
else:
    liquido=bruto-(bruto*(15/100))-(bruto*(7/100))
    if hrtrab>160:
        adicional=(bruto/160)*(50/100)*(hrtrab-160)
        print("Salario liquido de:",liquido,"com adicional de:",adicional)
    else:
        print("Salario liquido de:",liquido)
