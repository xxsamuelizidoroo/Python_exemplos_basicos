
# Importação da biblioteca
import math as m
# pi = 3.1415

# Coleta do valor do raio
raio = float(input("Informe o valor do raio: "))

# Cálculo
comp = 2 * m.pi * raio
# comp = 2 * pi * raio

# Resultado com 2 casas decimais
print(f"O perímetro da circunferência é {comp:.2f} cm.")
