salario = float(input('Qual é o seu salário bruto?\nR$'))

if salario <= 1903.98:
    salario_liquido = salario
    mensagem_isencao = "Você está isento(a) de imposto de renda."
else:
    if salario <= 2826.65:
        aliquota = 0.075
    elif salario <= 3751.05:
        aliquota = 0.15
    elif salario <= 4664.68:
        aliquota = 0.225
    else:
        aliquota = 0.275

    desconto_ir = salario * aliquota
    salario_liquido = salario - desconto_ir
    mensagem_isencao = ""

print(f'Seu salário líquido é R${salario_liquido:.2f}. {mensagem_isencao}')