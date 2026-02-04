"""
  _____                       _                              _         _ _      
 |  __ \                     (_)                            | |       | | |     
 | |__) |___  _ __ ___   __ _ _    ___ ______ _ _ __ ___    | | ____ _| | | __  
 |  _  // _ \| '_ ` _ \ / _` | |  / __|_  / _` | '_ ` _ \   | |/ / _` | | |/ /  
 | | \ \ (_) | | | | | | (_| | |  \__ \/ / (_| | | | | | |  |   < (_| | |   < _ 
 |_|  \_\___/|_| |_| |_|\__,_|_|  |___/___\__,_|_| |_| |_|  |_|\_\__,_|_|_|\_(_)
                                                                              
"""                                                                             

# itbetyar.hu - Romai szam kalkulator - 2023

# 1. Bekérünk egy romai szamot
rom = str(input("Add meg egy Római számot: "))
# 2. megszamoljuk a karaktereket
length = len(rom)
# 3. letrehozunk egy ures int(egesz szam) valtozot, amibe majd az osszeget irjuk
lnum = int(0)

# gyakorlashoz printelhetunk
# print(rom)
# print(length)

# dictionary resz a romai szam/ arab szam atalakito
# Itt tároljuk azt hogy melyik szám "mennyit ér"
roman_to_latin = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

# for ciklus, hogy az osszes beirt karakteren vegig menjunk
for i in range(length-1):
    #print(roman_to_latin[rom[i]])

    # Megnézzük, hogy az aktuális római szám értéke kisebb-e, mint az utána következőé
    # Példa: IV esetén az I (1) kisebb, mint a V (5)
    if roman_to_latin[rom[i]] < roman_to_latin[rom[i+1]]:
        # Ha kisebb előzi meg a nagyobbat, akkor le kell vonni az értékét
        # (Így lesz a IV-ből: -1 + 5 = 4)
        lnum -= roman_to_latin[rom[i]]
    else:
        # Ha az aktuális szám nagyobb vagy egyenlő, mint a következő, akkor simán hozzáadjuk
        # Példa: VI esetén a V (5) nagyobb, mint az I (1), tehát 5 + 1 = 6
        lnum += roman_to_latin[rom[i]]

# Mivel a ciklus az utolsó előtti karakterig futott (length-1), 
# a legutolsó számot a végén mindenképpen hozzá kell adnunk az összeghez.
lnum += roman_to_latin[rom[length - 1]]

print(f"A beirt római szám értéke: {lnum}")

# itbetyar.hu - Romai szam kalkulator - 2023
# itbetyar.hu - Romai szam kalkulator - 2023
# itbetyar.hu - Romai szam kalkulator - 2023

