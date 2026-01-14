#Ovo je lista (List)
poslovi = ["Nauci Git","Nauci Python","Napravi projekat"]

print("Tvoji trenutni zadaci su:")
# Ovo je petlja (LOOP) koja prolazi kroz listu
for posao in poslovi:
	print(f"- {posao}")
# Dodajemo novi zadatak preko terminala
novi_posao= input("Sta jos treba da uradis? ")
poslovi.append(novi_posao)

print(f"Sada imas Azuriranu listu zadatka: ")
for posao in poslovi:
	print(f"-{posao}")
