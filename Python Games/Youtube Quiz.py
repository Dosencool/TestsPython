print("Hallo , Herzlich WIllkommen zum Quiz!")
Ga1 = input("Beantworte die Fragen immer nur mit einer 1, 2, 3, 4…[ENTER]")
Ga2 = input("Bist du Bereit[ENTER]")

#Frage 1
print("Frage 1. Welche Nationalität hat der Stärkste Mann der Welt?")
print("1 U.S.A.")
print("2 China")
print("3 Luxembourg")
antwort = input("Eingabe: ")
if antwort =="3":
    print("Die Antwort ist Richig!")
elif antwort =="2":
    print("Die Antwort war Falsch!")
    quit()
elif antwort =="1":
    print("Die Antwort war Falsch!")
    quit()

#Frage 2
print("Wie hieß der Youtuber LUCA früher?")
print("1 Chockcrafter")
print("2 Concrafter")
print("3 Collcrafter")
antwort = input("Eingabe: ")
if antwort =="2":
    print("Die Antwort ist Richtig!")
elif antwort =="1":
    print("Die Antwort ist Falsch!")
    quit()
elif antwort =="3":
    print("Die Antwort ist Falsch!")
    # quit()