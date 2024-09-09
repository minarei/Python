p = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavras in p:
    print(f"\nNa palavra {palavras.upper()} temos: ", end = '')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print(letras, end = ' ')