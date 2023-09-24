# Romai-szam-atalakito
Speckó kalkulátorunkban a beírt római számot alakítjuk át 10-es számrendszerbe.

### Lecke nehézség: 3/10
### Igényelt tudásanyag:
For ciklus, index, dictionary

### Ennyi sor kódunk van: ~35

Egy kis kód elnőnézet:

<img src="https://github.com/itbetyar/romai-szam-atalakito/blob/main/romai-decimalis.jpg" alt="Alt text" width="400">

## Fontos részlet:
Mivel a római IV négyet jelent. Ha csak egyesével végigmennénk minden karakteren
és összeadnánk őket akkor ez hatot adna ki: 1 + 5 = 6;

Így a for ciklus egy összhasonlítással kezd. Párosával nézi a karaktereket és ha az első karakter értéke kisebb,
Akkor annak a karakternek az értékét kivonja a végső összegből.

Tehát: IV esetében összehasonlítja az 1-et és a 4-et. Mivel az első karakter értéke kisebb
az első karakter értékét kivonja az összegből. Mivel most kezdtünk számolni a végösszeg 0.
Ebből levon eggyet tehát -1 lesz az összeg. Majd a következő körben hozzáad 5-öt. 
A végösszeg = 4 = IV. Minden stimmel.
