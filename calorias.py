horas_de_exercicio = int(input('Quantas horas você praticou exercícios por semana? '))
calorias_por_semana = horas_de_exercicio * 60 * 5

calorias_por_mês = calorias_por_semana * 4

print(f"Por semana você gastou {calorias_por_semana:.2f} calorias\n Por mês você gastou {calorias_por_mês:.2f} calorias! Parabéns!")