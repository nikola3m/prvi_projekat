#Ovo je lista (List)
poslovi = ["Nauci Git","Nauci Python","Napravi projekat"]

print("Tvoji trenutni zadaci su:")
# Ovo je petlja (LOOP) koja prolazi kroz listu
for posao in poslovi:
	print(f"- {posao}")
# Dodajemo novi zadatak preko terminala
novi_posao= input("Sta jos treba da uradis? ")
poslovi.append(novi_posao)

print(f"Sada imas {len(poslovi)} zadatka: ")
#Logika: Ako imas puno dazadata, ispisi upozorenje
if len(poslovi) > 3:
	print("Vreme je za pauzu, impas previse posla!")
else:
	print("Samo napred, mozes jos nesto dodati!")
#Konacan ispis koda
print("Konacna lista obaveza: ")
for posao in poslovi:
	print(f"-{posao}")
