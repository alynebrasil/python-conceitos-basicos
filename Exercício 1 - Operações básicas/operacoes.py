numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
#Se o número 2 for 0, imprimimos uma mensagem dizendo que é impossível dividir por 0, evitando o erro
divisao = "impossível, pois não se pode dividir por 0" if numero2 == 0 else int(numero1 / numero2)

print(f'A soma desses números é igual a {soma}\nSubtraindo o segundo do primeiro temos:{subtracao}\nA multiplicação desses números é igual a {multiplicacao}\nE por fim, a divisão desses é {divisao}')