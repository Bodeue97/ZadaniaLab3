from random import randint
# # Zad1
#
#
# a = [ 1 -x for x in  range(1, 11, 1)]
# print(a)
#
# b = [ 4**y for y in range(8)]
# print(b)
#
# c = [x for x in b if x % 2 == 0]
# print(c)

# # Zad2
# randList = [randint(0, 100) for x in range(10)]
# randList.sort()
# print(randList)
#
# evenRand = [x for x in randList if x%2==0]
# print(evenRand)

# # Zad3
#
# produkty = {"jablka":"Kg", "jaja":"paczka", "gazeta wybiórcza":"szt","Majonez Kętrzyński":"szt"}
# print(produkty)
#
# prodSzt = [produkt for produkt in produkty.keys() if produkty[produkt] =="szt"]
# print(prodSzt)


# # Zad4

# def isRightAngle(a, b, c):
#         if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(c).isdigit() == False):
#             return "Podano bledne wartosci"
#         else:
#             a = float(a)
#             b = float(b)
#             c = float(c)
#             if (a<=0)|(b<=0)|(c<=0):
#                 return "Podano bledne wartosci"
#             elif (a > b) & (a > c):
#                 check = b**2 + c**2
#                 if a**2 == check:
#                     return "Trojkat jest prostokatny"
#                 else:
#                     return "Trojkat nie jest prostokatny"
#             elif (b > a) & (b > c):
#                 check = a**2 + c**2
#                 if b**2 == check:
#                     return "Trojkat jest prostokatny"
#                 else:
#                     return "Trojkat nie jest prostokatny"
#             else :
#                 check = b ** 2 + a ** 2
#                 if c ** 2 == check:
#                     return "Trojkat jest prostokatny"
#                 else:
#                     return "Trojkat nie jest prostokatny"
#
#
#
# a = input("Podaj dlugosc pierwszego boku trojkata: \n")
# b = input("Podaj dlugosc drugiego boku trojkata: \n")
# c = input("Podaj dlugosc trzeciego boku trojkata\n")
# print(isRightAngle(a, b, c))


# # Zad5
#
#
#
# def trapField(a, b, h):
#     if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(h).isdigit() == False):
#         return "Podano bledne wartosci"
#     else:
#         a = float(a)
#         b = float(b)
#         h = float(h)
#         if (a<=0)|(b<=0)|(h<=0):
#             return "Podano bledne wartosci"
#         else:
#             P = (a+b)*h/2
#             return P
#
#
# a = input("Podaj dlugosc pierwszej podstawy trapezu\n")
# b = input("Podaj dlugosc drugiej podstawy trapezu\n")
# h = input("Podaj wysokosc trapezu\n")
# print(trapField(a, b, h))

# Zad6


