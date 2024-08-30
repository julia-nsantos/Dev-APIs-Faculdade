
# 1) Desenvolva um código python que calcula o peso ideal de 100 pessoas. Deve receber
# a altura e o sexo. Usar um loop para validar se o sexo está correto (H ou M).
# para Homens: Peso Ideal = (72.7*altura) - 58
# para Mulheres: Peso Ideal = (62.1*altura) - 44.

def calcular_peso_ideal():
    pessoas = 100
    pesos_ideais = []

    for i in range(pessoas):
        altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
        sexo = input(f"Digite o sexo da pessoa {i+1} (H para homem, M para mulher): ").upper()

        while sexo not in ['H', 'M']:
            print("Sexo inválido! Digite 'H' para homem ou 'M' para mulher.")
            sexo = input(f"Digite o sexo da pessoa {i+1} (H para homem, M para mulher): ").upper()

        if sexo == 'H':
            peso_ideal = (72.7 * altura) - 58
        elif sexo == 'M':
            peso_ideal = (62.1 * altura) - 44

        pesos_ideais.append(peso_ideal)
        print(f"O peso ideal para a pessoa {i+1} é: {peso_ideal:.2f} kg")

    return pesos_ideais

pesos = calcular_peso_ideal()