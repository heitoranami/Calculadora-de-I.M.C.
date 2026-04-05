peso = float(input("Qual seu peso em Kg? ="))
altura = float(input("Qual sua altura em M? ="))
pas1 = altura * altura
pas2 = peso / pas1


formIMC = pas2


if formIMC < 18.5:
  print("classificação = Baixo Peso")
  print("Risco De Comorbidades = Baixo")
  print("FórmulaIMC = ", formIMC)

elif formIMC <= 24.9:
  print("classificação = Peso Normal")
  print("Risco De Comorbidades = Médio")
  print("FórmulaIMC = ", formIMC)

elif formIMC <= 29.9:
  print("classificação = Pré-Obeso")
  print("Risco De Comorbidades = Aumentado")
  print("FórmulaIMC = ", formIMC)

elif formIMC <= 34.9:
  print("classificação = Obeso I")
  print("Risco De Comorbidades = Moderado")
  print("FórmulaIMC = ", formIMC)

elif formIMC <= 39.9:
  print("classificação = Obeso II")
  print("Risco De Comorbidades = Grave")
  print("FórmulaIMC = ", formIMC)

else:
  print("classificação = Obeso III")
  print("Risco De Comorbidades = Muito Grave")
  print("FórmulaIMC = ", formIMC)