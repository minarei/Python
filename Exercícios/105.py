def notas(*n, sit = False):
    """
    Função que agrupa diversas notas de um aluno num dicionário contendo informações relacionadas ao mesmo.
    -> Total: Total de notas do aluno.
    -> Maior: Maior nota do aluno.
    -> Menor: Menor nota do aluno.
    -> Média: Média do aluno.
    -> Situação: Situação do aluno (boa, razoável ou ruim).
    """
    aluno = {}
    aluno["total"] = len(n)
    aluno["maior"] = max(n)
    aluno["menor"] = min(n)
    aluno["média"] = (sum(n)) / len(n)
    
    if sit:
        if aluno["média"] >= 7:
            aluno["situação"] = "Boa"
        elif aluno["média"] < 7 and aluno["média"] > 5:
            aluno["situação"] = "Razoável"
        else:
            aluno["situação"] = "Ruim"
    return aluno
    
r = notas(2, 6, sit = True)
print(r)