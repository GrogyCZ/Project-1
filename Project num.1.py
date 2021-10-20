# Projekt num. 1 - Jídelníček automat

# Níže jsem definoval základní atributy se kterými budu následovně pracovat.
template_q = "Zadej {} klienta{}"
template_a = "Neplatná odpověď. Zadej platnou odpověď."

name = input(template_q.format("jméno", ":"))

while True:
    try:
        age = int(float(input(template_q.format("věk", ":"))))  # převod ze str na int jsem si dohledal na internetu
        break
    except ValueError:
        print(template_a)

while True:
    gender = str(input(template_q.format("pohlaví", ":")))
    gender = gender.lower()
    isMan = None
    if gender != "muž" and gender != "m" and gender != "žena" and gender != "ž":
        print(template_a)
    elif gender == "muž" or gender == "m":
        isMan = True
        break
    elif gender == "žena" or gender == "ž":
        isMan = False
        break

while True:
    try:
        height = int(float(input(template_q.format("výšku", " v cm:"))))
        if height > 270 or height < 55:
            print(template_a)
        else:
            break
    except ValueError:
        print(template_a)

while True:
    try:
        weight = int(float(input(template_q.format("váhu", "v kg:"))))
        if weight < 635:
            break
        else:
            print(template_a)
    except ValueError:
        print(template_a)

while True:
    sport_lvl = str(input(template_q.format("kategorii sportovní vyspělosti", "- Začátečník, Pokročilý, "
                                                                              "Zkušený:")))
    sport_vysp = sport_lvl.lower()
    if sport_lvl != "začátečník" and sport_vysp != "z" and sport_vysp != "pokročilý" and \
            sport_vysp != "p" and sport_vysp != "zkušený" and sport_vysp != "zk":
        print(template_a)
    else:
        break

B = ["začátečník", "z"]
I = ["pokročilý", "p"]
E = ["zkušený", "zk"]

while True:
    try:
        body_fat = int(float(input(template_q.format("odhad množství tělesného tuku", " v procentech:"))))
        body_fat = body_fat / 100
        break
    except ValueError:
        print(template_a)

# Níže jsou použity dvě rovnice na výpočet bazálního metabolismu a průměr jejich výsledků je dále používán

HB_male = 0
HB_female = 0
MS_male = 0
MS_female = 0

# Revidovaná Harris-Benediktova rovnice
# if = rovnice pro muže/else = rovice pro ženu:
if isMan:
    HB_male = 13.397 * weight + 4.799 * height - 5.667 * age + 88.362
else:
    HB_female = 9.247 * weight + 3.1 * height - 4.33 * age + 447.593

# Mifflin-St Jeorova rovnice
# if = rovnice pro muže/else = rovice pro ženu:
if isMan:
    MS_male = 10 * weight + 6.25 * height - 5 * age + 5
else:
    MS_female = 10 * weight + 6.25 * height - 5 * age + 161

# průměr rovnice

BM_male = (HB_male + MS_male) / 2
BM_female = (HB_female + MS_female) / 2

# odečtení tělesného tuku

BM_male = BM_male - BM_male * body_fat
BM_female = BM_female - BM_female * body_fat

# Průměrný termální efekt, který vzniká pří rozkladu potravin. Jedná se o energii potřebnou k rozložení potravy.
T_effect = 1.05

# Stanovení míru denní aktivity

print(" ")
print("""
Vyber podle číslovky sportovní typ, který nejvíce odpovídá životnímu stylu klienta:

1)sedavý typ - minimální nebo žádný pohyb.
2)lehce aktivní typ - cvičení 1 až 3 dny v týdnu.
3)mírně aktivní typ - cvičení 3 až 5 dní v týdnu.
4)velmi aktivní typ - pravidelné cvičení 5 až 6 v týdnu + celkově aktivní životní styl.
5)extra aktivní typ - pokud se jedná o profesionálního sportovce ve vrcholné přípravě, který pravidelně trénuje 6 
až 7 dní v týdnu.
""")

while True:
    try:
        aktiv_typ = int(float(input(template_q.format("míru aktivity", ":"))))
        if aktiv_typ == 1:
            aktiv_typ = 1.2
            break
        elif aktiv_typ == 2:
            aktiv_typ = 1.375
            break
        elif aktiv_typ == 3:
            aktiv_typ = 1.55
            break
        elif aktiv_typ == 4:
            aktiv_typ = 1.725
            break
        elif aktiv_typ == 5:
            aktiv_typ = 1.9
            break
        else:
            print("Neplatná hodnota. Zadej skutečnou hodnotu.")
    except ValueError:
        print("Neplatná hodnota. Zadej skutečnou hodnotu.")
print(" ")

total_male = round(BM_male * T_effect * aktiv_typ)
total_female = round(BM_female * T_effect * aktiv_typ)
if isMan:
    print("Denní kalorický příjem klienta jménem " + name + " činí " + str(total_male) + " kcal.")
else:
    print("Denní kalorický příjem klientky jménem " + name + " činí " + str(total_female) + " kcal.")

print(" ")

# Níže program rozděluje kalorie do specifických makronutrientů podle cvičenosti klienta
proteins = 0
carbs = 0
fats = 0


def makro(sex, percent, value):
    return round((sex * percent) / value)


def makro_split():
    global proteins, carbs, fats
    if sport_lvl in B:
        if isMan:
            proteins = makro(total_male, 0.2, 4)
            carbs = makro(total_male, 0.6, 4)
            fats = makro(total_male, 0.2, 9)
        else:
            proteins = makro(total_female, 0.2, 4)
            carbs = makro(total_female, 0.6, 4)
            fats = makro(total_female, 0.2, 9)
    elif sport_lvl in I:
        if isMan:
            proteins = makro(total_male, 0.25, 4)
            carbs = makro(total_male, 0.5, 4)
            fats = makro(total_male, 0.25, 9)
        else:
            proteins = makro(total_female, 0.25, 4)
            carbs = makro(total_female, 0.5, 4)
            fats = makro(total_female, 0.25, 9)
    elif sport_lvl in E:
        if isMan:
            proteins = makro(total_male, 0.3, 4)
            carbs = makro(total_male, 0.45, 4)
            fats = makro(total_male, 0.25, 9)
        else:
            proteins = makro(total_female, 0.3, 4)
            carbs = makro(total_female, 0.45, 4)
            fats = makro(total_female, 0.25, 9)


makro_split()

if isMan:
    print(
        "Rozložení makronutrientů pro klienta jménem {0} na celkový denní příjem {1} kcal: "
        "Bíloviny = {2} , Sacharidy = {3} , Tuky = {4}.".format(
            name, str(total_male), str(proteins), str(carbs), str(fats)))
else:
    print(
        "Rozložení makronutrientů pro klientky jménem {0} na celkový denní příjem {1}kcal: "
        "Bíloviny = {2}g , Sacharidy = {3}g , Tuky = {4}g.".format(
            name, str(total_female), str(proteins), str(carbs), str(fats)))

