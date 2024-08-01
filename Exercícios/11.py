lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
are = lar * alt
tin = are / 2

print("Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}m²." .format(lar, alt, are))
print("Para pintar essa parede, você precisará de {:.4f} litros de tinta." .format(tin))