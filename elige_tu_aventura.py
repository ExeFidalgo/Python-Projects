name = input("Escribe tu nombre: ")
print("Bienvenida/o", name, "a esta aventura magica!")

answer = input("Estas en una casa embrujada, hay un fantasma detras tuyo. Escapas por el pasillo o por el patio? ").lower()

if answer == "pasillo":
     answer = input ("El fantasma corre detras tuyo, gritas pero nadie te escucha. Golpeas al fantasma o rezas?").lower()

     if answer == "rezo":
        print("El fantasma te muerde una teta")
     elif answer == "golpeo":
        print("el fantasma te muerde la cola")
     else:
        print("Escribiste una opcion invalida. Alpiste perdiste!")
elif answer == "patio":
    print("corre wachin! que te alcanza el gua gua! ")
else:
    print("Escribiste una opcion invalida. Alpiste perdiste!")