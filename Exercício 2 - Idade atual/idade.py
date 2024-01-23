

from datetime import datetime

# Solicita ao usuário que insira a data de nascimento
data_nascimento_str = input('Digite sua data de nascimento no formato (YYYY-MM-DD): ')

# Converte a string de data de nascimento para um objeto datetime
data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d')

# Data atual
data_atual = datetime.now()

# Calcula a diferença entre as datas
diferenca = data_atual - data_nascimento

# Obtém a idade em anos
idade = diferenca.days // 365

print(f'Sua idade é: {idade} anos')