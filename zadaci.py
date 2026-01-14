# DEFINISANJE FUNKCIJA
def ispisi_listu(lista_zadataka):
	print("\n--- TVOJI ZADACI ----")
	for posao in lista_zadataka:
		print (F"[*]{posao}")
	print("---------\n")

# Glavni deo programa , definisanje liste i poziv funkcije

poslovi = ["Nauci GIT","Ncti Python"]

ispisi_listu(poslovi) #Poziv funkcije da ispise predefinisanu listu

novi = input("Dodaj novi zadatak na listu: ")
poslovi.append(novi)

ispisi_listu(poslovi) # Drugi poziv funkcije (isti kod, drugi prolaz ispis sa novim zadatkom)

