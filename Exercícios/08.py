d = float(input("Uma distância em metros: "))

print("A medida de {:.1f} corresponde a: " .format(d))
print("{}km" .format(d / 1000))
print("{}hm" .format(d / 100))
print("{}dam" .format(d / 10))
print("{}dm" .format(d * 10))
print("{}cm" .format(d * 100))
print("{}mm" .format(d * 1000))