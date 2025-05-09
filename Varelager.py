varer = []  # Liste for å lagre varer

def printMeny():
    print("-------Lagersystem-------")
    print(" 1. Legg til ny vare     ")
    print(" 2. Søk etter vare       ")
    print(" 3. Oppdater antall vare ")
    print(" 4. Slett vare           ")
    print(" 5. Se registrerte varer ")
    print(" 6. Avslutt              ")

    menyValg = input("Velg et tall mellom 1-6.")
    menyValgt(menyValg)

def menyValgt(menyValg):
    if menyValg == "1":
        registrer_vare()
    elif menyValg == "4":
        slett_vare()
    elif menyValg == "5":
        vis_varer()
    elif menyValg == "6":
        print("Avslutter programmet.")
        exit()
    else:
        print("Ugyldig valg, prøv igjen.")
        printMeny()

def registrer_vare():
    varenummer = input("Skriv inn varenummer: ")
    navn = input("Skriv inn navn: ")
    kategori = input("Skriv inn kategori: ")
    antall = input("Skriv inn antall: ")
    pris = input("Skriv inn pris: ")

    # Opprett en dictionary for varen og legg den til i listen
    vare = {
        "varenummer": varenummer,
        "navn": navn,
        "kategori": kategori,
        "antall": antall,
        "pris": pris
    }
    varer.append(vare)
    print("Varen er registrert!")
    printMeny()

def vis_varer():
    if not varer:
        print("Ingen varer registrert.")
    else:
        print("Registrerte varer:")
        for vare in varer:
            print(f"Varenummer: {vare['varenummer']}, Navn: {vare['navn']}, Kategori: {vare['kategori']}, Antall: {vare['antall']}, Pris: {vare['pris']}")
    printMeny()

def slett_vare():
    varenummer = input("Skriv inn varenummeret til varen du vil slette: ")
    for vare in varer:
        if vare["varenummer"] == varenummer:
            varer.remove(vare)
            print(f"Varen med varenummer {varenummer} er slettet.")
            break
    else:
        print(f"Fant ingen vare med varenummer {varenummer}.")
    printMeny()

printMeny()