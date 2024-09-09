aluno = {'Nome': str(input("Nome: ")), 'Média': float(input("Média: "))}

print(f"O nome do aluno é {aluno["Nome"]}.")
print(f"A média do aluno é {aluno["Média"]}.")

if aluno["Média"] >= 6:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'

print(f"A situação do aluno é {aluno["Situação"]}.")