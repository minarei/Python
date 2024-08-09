s = str(input("Informe seu sexo: ")).strip().upper()[0]

while s not in 'MF':
    s = str(input("Dados inválidos. Por favor, informe-os corretamente: ")).strip().upper()[0]

print(f"Sexo {s} registrado com sucesso.")