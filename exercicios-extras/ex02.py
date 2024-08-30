
# 2) Faça um programa que receba a temperatura média de cada mês do ano e armazene-
# as em um dicionário.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima
# da média anual, e em que mês elas ocorreram.

def temperaturas_anuais():
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    temperaturas = {}

    for mes in meses:
        temp = float(input(f"Digite a temperatura média de {mes}: "))
        temperaturas[mes] = temp

    media_anual = sum(temperaturas.values()) / 12
    print(f"\nA média anual das temperaturas é: {media_anual:.2f}°C\n")

    print("Meses com temperaturas acima da média anual:")
    for mes, temp in temperaturas.items():
        if temp > media_anual:
            print(f"{mes}: {temp:.2f}°C")

temperaturas_anuais()