nota1 = float(input('Coloque a primeira nota: '))
nota2 = float(input('Coloque a segunda nota: '))

result1 = nota1 + nota2
resultf = result1 / 2

if resultf >= 7:
    print(f'Aprovado!! Sua média foi: {resultf}')
elif resultf < 5:
    print(f'Reprovado!! Sua nota não atingiu a média: {resultf}')
elif resultf >= 5 and resultf < 7:
    print(f'Recuperação!! Sua média foi: {resultf}') 
