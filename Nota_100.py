nota = input("Ingrese la nota del examen desde 0 hasta 100\n")
nota = int(nota)

if nota >= 90 and nota < 101:
    print("La nota es A")
elif nota < 90 and nota >= 80:
    print ("La nota es B")
elif nota < 80 and nota >= 70:
    print ("La nota es C")
elif nota < 70 and nota >= 60:
    print ("La nota es D")
elif nota < 60 and nota >= 0:
    print ("La nota es F")