import os
clear = lambda: os.system("cls")

Name = input("Wie heißt du? ")
print("Hallo "+Name)

level = 0
print("Hallo, Herzlich Willkommen zu meinem Spiel!")
Game = input("Du hast ein paar Antworten, du musst einfach die richtige nummer eingeben. Du hast nur ein leben, Viel Spaß![ENTER]")

erl = input("Herzlich Willkommen zum ersten Level vom Spiel Secret Man![ENTER]")
print("Frage 1. Es ist Nacht, wo willst du hingehen?")
print("1. Nach Hause schlafen gehen.")
print("2. Eine fremde burg spionieren gehen.")
eins = input ("Eingabe: ")
if eins =="2":
  eins = input("Richtige Antwort! Du  gehst nun zur Burg.[ENTER]")
elif eins =="1":
  eins = input("Du gehst zu dir nach Hause, aber leider wirst du von einem riesigen Monster gefressen der vor deinem Haus gewartet hat. Deine Antwort war Falsch![ENTER]")
  print("Du musst leider wieder von vorne anfangen.")
  quit()
print("Frage 3. Du bist im Schloss ,und vor dir sind drei Türen. In der ersten Tür ist ein proffessionneller Mörder aus dem Jahr 1555. In der zweiten Tür ist überall Feuer und in der Dritten Tür sind viele hungrige giftige Schlangen.")
print("Frage 2. Du bist bei der Burg angekommen, die Tür ist nicht bewacht, wie willst du rein gehen?")
print("1. Du sagst: Sesam öffne dich!")
print("2. Du nimmst ein Hammer und machst die Tür kaputt!")
print("3. Du machst die Tür mit den Händen auf!")
zwei = input("Eingabe: ")
if zwei == "2":
  zwei = input("Du machst die Tür kaputt du gehst rein und bemerkst dass die Tür auf war, aber mindenstens bist du drinnen! Die Antwort war Richtig![ENTER]")
elif zwei =="1":
  zwei = input("Du sagst Sesam öffne dich, die Tür öffnet sich trifft dein Kopf, du bist füür zwei Stunden K.O. und die Tür schließt sich nach wenige Sekunden. Dein Antwort ist Falsch![ENTER]")
  clear()
  quit()
elif zwei =="3":
  zwei = input("Du machst die Tür mit deinen Händen auf, aber leider hast du einen geheimen Knopf gedrückt der einen Hammer auslöst. Du bist füür zwei Stunden K.O. und die Tür schließt sich. Die Antwort war Falsch[ENTER]")
  clear()
  quit()
print("Welche Tüür nimmst du? du kannst auch")
print("1. den Mörder")
print("2. das Feuer")
print("3. die Schlangen")
drei = input("Eingabe: ")
if drei =="1":
  drei = input("Ein Mörder aus dem Jahr 1555 wäre jetzt 465 Jahre alt also schon lange tot. Deine Antwort ist Richtig![ENTER]")
elif drei =="2":
  drei = input("Beim Feuer könntest du nicht durch gehen deine überlebens-chancen wären zu klein. Die Antwort war Falsch.[ENTER]")
  clear()
  quit()
elif drei == "3":
  drei = input("Die Schlangen würden vergiften und du würdest sterben. Die antwort war Falsch.[ENTER]")
  clear()
  quit()
print("Hinter den Türen ist der König, du spionnierst ihn aus!")
print("Du hast den Level 1 geschafft!")
Level = 1

print("Hallo, Herzlich Willkommen zum zweiten Level!")
zwl = input("Bist du Bereit?[ENTER]")
print("Los geht's")
print("Du bist in der Schule, du musst probieren auszubrechen!")
print ("Was willst du machen? ")
print("1. Aus dem lüftungsschach klettern")
print("2. Aus dem Fenster springen")
einsa = input("Eingabe: ")
if einsa == "1":
    print("Du gehst ins lüftungsschach und kletters dich durch. Die Antwort war Richtig!")
elif einsa == "2":
    print("Du springst zur Fenster Raus, brechst dir ein Arm und beim weinen erwischt der Direktor dich! Die antwort war Falsch!")
    quit()
print("Du bist durch geklettert, und am Ende sind zwei Lüftungsschachtüren beim eine sind zwei Hünde, aber ihre Hunderasse ist gefährlich und beim anderen ein Polizist!")
print("Wo gehst du durch?")
print("1. Beim Polizist")
print("2. Bei den Hünden")
einsb = input("Eingabe: ")
if einsb == "1":
    print("Du gehst durch, der Polizist seht dich und bringt dich zum direktor. Die Antwort war Falsch!")
    quit()
elif einsb == "2":
    print("Du gehst durch aber dir passiert nichts, weil ich habe gesagt ihre Hunderasse wäre gefährlich aber ich sagte nie dass sie gefährlich wären, sie wurden nähmlich als Haushunde dressiert. Die Antwort war Richtig!")
print("Du bist nun auf dem Dach von der Schule, wie willst du runter gehen?")
print("1. Du springst ins Schwimmbad der Nachbarin")
print("2. Du springst auf den Trampolin vor der Schule, der im Boden eingebaut ist. Du musst aufpassen es ist nämlich schon gras drübergewachsen.")
einsc = input("Eingabe: ")
if einsc == "1":
    print("Du springst drin die Polizei sieht dich und nimmt dich Fest. Die Antwort ist Falsch!")
    quit()
elif einsc == "2":
    print("Du springst drauf und laufst weg! Die antwort war Richtig")
print ("Du hast den Level geschafft!")
level = 2

print("Toll, du hast das Quiz geschafft")