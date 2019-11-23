miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")

while True:
    try:
        dystans_ab = float((input(f"Dystans {miasto_a}-{miasto_b}: ")))
        break
    except:
        print("Nie podałeś liczby!")
        continue

while True:
    cena_paliwa = float(input("Cena paliwa: "))
    if cena_paliwa  == isinstance(cena_paliwa,float):
        break
    else:
        continue




spalanie = float((input("Spalanie na 100km: ")))
spalanie_100 = dystans_ab / 100 * cena_paliwa * spalanie





print(f"""Miasto A: {miasto_a}
Miasto B: {miasto_b}
Dystans {miasto_a}-{miasto_b}
Cena paliwa: {cena_paliwa}
Spalanie na 100km: {spalanie}""")

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {int(spalanie_100)} PLN")