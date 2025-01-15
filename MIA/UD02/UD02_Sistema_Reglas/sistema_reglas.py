
def selecte_transport(distance, hurry, money,sustainable):
    vehicle = ""
    if distance <= 1:
        if hurry:
            vehicle = "Patinete eléctrico"
        else:
            vehicle = "Caminar"

    elif distance <= 5:
        if hurry:
            vehicle = "Bicicleta"
        else:
            if money:
                vehicle = "Bicicleta"
            else:
                vehicle = "Bus"
        
    elif distance <= 50:
        if hurry:
            vehicle = "Coche"
        else:
            if money:
                vehicle = "Coche"
            else:
                vehicle = "Bus"

    else:
        if hurry:
            vehicle = "Coche"
        else:
            if money:
                vehicle = "Coche"
            else:
                if sustainable:
                    vehicle = "Tren"
                else:
                    vehicle = "Coche"
    return vehicle

distance = 1
hurry = False
money = False
sustainable = False
example1 = selecte_transport(distance, hurry, money, sustainable)
print(f"Te recomendamos usar el {example1} para tu viaje")

distance = 52
hurry = False
money = False
sustainable = True
example2 = selecte_transport(distance, hurry, money, sustainable)
print(f"Te recomendamos usar el {example2} para tu viaje")
