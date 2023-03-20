midiccionario = {"nombre": "Exe", "edad": 36, "ciudad": "Libertad"}
print(midiccionario)

midiccionario2 = dict(nombre = "Vanesa", edad = 44, ciudad = "Libertad")
print(midiccionario2)

midiccionario["email"] = "exekover@gmail.com"
print(midiccionario)

del midiccionario ["email"]
print(midiccionario)

midiccionario.pop("edad")
print(midiccionario)