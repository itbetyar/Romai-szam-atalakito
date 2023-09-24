# itbetyar.hu - Romai szam kalkulator - 2023
# 1. bekerjuk a romai szamot
rom = str(input("Add meg egy Római számot: "))
# 2. megszamoljuk a karaktereket
length = len(rom)
# 3. letrehozunk egy ures int valtozot, amibe majd az osszeget irjuk
lnum = int(0)

# gyakorlashoz printelhetunk
# print(rom)
# print(length)

# dictionary resz a romai szam/ arab szam atalakito
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
    if roman_to_latin[rom[i]] < roman_to_latin[rom[i+1]]:
        lnum -= roman_to_latin[rom[i]]
    else:
        lnum += roman_to_latin[rom[i]]

lnum += roman_to_latin[rom[length - 1]]

print(f"A beirt római szám értéke: {lnum}")








