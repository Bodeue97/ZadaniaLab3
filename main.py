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
# def trapField(a=1, b=1, h=1):
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
# print(trapField())
# a = input("Podaj dlugosc pierwszej podstawy trapezu\n")
# b = input("Podaj dlugosc drugiej podstawy trapezu\n")
# h = input("Podaj wysokosc trapezu\n")
# print(trapField(a, b, h))



# # Zad6
# #Nie byłem w 100% pewny co trzeba zrobić w zadaniu, więc zrobiłem funkcję, która oblicza iloczyn n pierwszych elementow ciagu geometrycznego
#
#
# def seqProd(a1=1, q=4, n=10):
#     an = a1*q
#     elCiagu = []
#     elCiagu.append(a1)
#     elCiagu.append(an)
#     iloczyn = a1*an
#     for x in range (3, n+1, 1):
#         anp1 = an * q
#         elCiagu.insert(x, anp1)
#         an = anp1
#         iloczyn *= anp1
#
#     return iloczyn, elCiagu
# print(seqProd(1, 2, 6))


# # Zad7
#
# def seqProdUnl(* elementy):
#     if(len(elementy) != 0):
#         iloczyn = 1
#         for x in range(len(elementy)):
#             iloczyn*=elementy[x]
#         return iloczyn
#     else:
#         return 0
# print(seqProdUnl(1, 2, 3, 4, 5, 6))


