import pygame

Ga1 = input("Herzlich WIllkommen zum Test der Idioten.[ENTER]")
Ga2 = input("Normalerweise müsste jeder den Test ohne Fehler hinbekommen.[ENTER]")
Ga3 = input("Du musst immer mit nur einem Wort antworten![ENTER]")
Ga4 = input("Bist du Bereit?[ENTER]")

aa1 = input("Fangen wir mit der ersten Frage an.[ENTER]")
print("1. BIst du ein 1% schlau oder 1% dumm?")
print("Hier musst du mit 1% schlau oder 1% dumm antworten")
antwort = input("Eingabe: ")
if antwort =="1% schlau":
    print("Die Antwort ist Falsch, weil wenn du 1% schlau bist, bist du du 99% dumm!")
    quit()
elif antwort =="1% dumm":
    print("Die Antwort ist Richtig, weil wenn man 1% dumm ist, ist man 99%schlau!")
    