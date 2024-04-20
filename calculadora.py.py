import math

print("dame un numero")
numero1 = int(input())
print("dame otro numero")
numero2 = int(input())

print("\nelige una operacion")
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
print("5.raiz cuadrada")
print("6.potencia")
print("7.seno")
print("8.coseno")
print("9.tangente\n")

opcion = int(input())
if opcion == 1:  #suma
  print("\nla suma es:", numero1 + numero2)

elif opcion == 2:  #resta
  print("\nla resta es:", numero1 - numero2)

elif opcion == 3:  #multiplicacion
  print("\nla multiplicacion es:", numero1 * numero2)

elif opcion == 4:  #division
  print("\nla division es", numero1 / numero2)

elif opcion == 5:  #raiz cuadrada
  print("\nde que numero quieres la raiz cuadrada:")
  print("1. primer numero")
  print("2. segundo numero")
  opcion = int(input())
  if opcion == 1:
    print("\nla raiz cuadrada es:", math.sqrt(numero1))
  elif opcion == 2:
    print("\nla raiz cuadrada es:", math.sqrt(numero2))

elif opcion == 6:  #potencia
  print("\nde que numero quieres la potencia:")
  print("1. primer numero")
  print("2. segundo numero\n")
  opcion = int(input())
  if opcion == 1:
    print(
        "\ningresa la potencia a la que que quieres que se eleve el primer numero"
    )
    potencia1 = int(input())
    print("\nla potencia es:", numero1**potencia1)

  elif opcion == 2:
    print(
        "\ningresa la potencia a la que quieres que se eleve el segundo numero"
    )
    potencia2 = int(input())
    print("\nla potencia es:", numero2**potencia2)

elif opcion == 7:  #seno
  print("\nde que numero quieres el seno:")
  print("1. primer numero")
  print("2. segundo numero\n")
  opcion = int(input())
  if opcion == 1:
    print("\nel seno es:", math.sin(numero1))
  elif opcion == 2:
    print("\nel seno es:", math.sin(numero2))

elif opcion == 8:  #coseno
  print("\nde que numero quieres el coseno:")
  print("1. primer numero")
  print("2. segundo numero\n")
  opcion = int(input())
  if opcion == 1:
    print("\nel coseno es:", math.cos(numero1))
  elif opcion == 2:
    print("\nel coseno es:", math.cos(numero2))

elif opcion == 9:  #tangente
  print("\nde que numero quieres la tangente:")
  print("1. primer numero")
  print("2. segundo numero\n")
  opcion = int(input())
  if opcion == 1:
    print("\nla tangente es:", math.tan(numero1))
  elif opcion == 2:
    print("\nla tangente es:", math.tan(numero2))
