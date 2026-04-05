# Calculador de I.M.C. (Índice de Massa Corpórea)


Projeto criado no curso de Programação Nível 1 NAAHs


## Cálculo do I.M.C.
	O calculo do I.M.C. é feito a partir de duas informações: Peso e Altura.
	Após dado os valores, devemos elevar a Altura pelo quadrado (X²),depois dividi-lá pelo Peso.
	Observe: 
###### (P)Peso: 50 Kg/ (A)Altura: 1.60 M
###### ((A * A) / P) R:19.53124999...


## Classificação pelo Resultado
	Para classificarmos devemos analizar a tabela de classificação de Risco de Comorbidades(Baixo/Alto/Moderado/...) e Classe(Peso:Normal/Baixo/Pré-Obeso/...).
	Observe:
 IMC (kg/m²)        | Classificação      | Risco de comorbidades
  "Abaixo de 18,5"  |  Abaixo do peso    |  Risco de comorbidades Baixo 
  "18,5 – 24,9"     |  Peso normal       |  Risco de comorbidades Médio
  "25,0 – 29,9"     |  Sobrepeso         |  Risco de comorbidades Aumentado
  "30,0 – 34,9"     |  Obesidade Grau I  |  Risco de comorbidades Moderado
  "35,0 – 39,9"     |  Obesidade Grau II |  Risco de comorbidades Grave
  "Maior que 40,0"  |  Obesidade Grau III|  Risco de comorbidades Muito grave 


## Código com explicações:
```python
#Definição das variáveis
peso = float(input("Qual seu peso em Kg? ="))
altura = float(input("Qual sua altura em M? ="))

#Obs: float = número decimal / int = número inteiro

#Contas
pas1 = altura * altura
pas2 = peso / pas1

#Dando o valor do passo 2 à variável formIMC
formIMC = pas2

#Classificação de acordo com a variável formIMC
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
```