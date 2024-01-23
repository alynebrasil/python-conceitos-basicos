try:
    ganho_por_hora = float(input('Quanto você ganha por hora? (exemplo: R$12.50)\n>>R$'))
    horas_trabalhadas = int(input('Quantas horas você trabalhou esse mês?\n'))
except ValueError:
    print('Por favor, insira um valor válido para o cálculo do salário. Exemplo: 12.50')
    exit()

salario_do_mes = ganho_por_hora * horas_trabalhadas

print('Seu salário mensal é: ', salario_do_mes)