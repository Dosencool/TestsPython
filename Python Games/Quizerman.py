ga1 = input("Bonjour, Bienvenue au Quizgame!ENTER")
print("Quel est votre non?")
nom = input("Réponse: ")
print("Bonjour "+nom)
  


rep0 = True
while(rep0):
  ga2 = input("Bienvenue à la première question!ENTER")
  rep1=True
  while(rep1):
    print("Première Question = Tu est dans une maison sans Électricité. Tu veux sortir. Il y a trois Portes.Dans la première Porte il y a du Feu partout! Dans la deuxième Porte il y a un Piége Électric qui te tue diréctement! Dans la troisième Porte il y a du Gase qui te tue! Quel Porte prend tu?")
    print("1 Le Feu")
    print("2 Le Piége")
    print("3 Le Gase")
    reponse = input("Réponse: ")
    if reponse=="2":
       print("Correct, La Réponse est 2 , car il y a pas d'Électricité!")
       rep1=False
    elif reponse =="1":
      print("La Réponse est fausse!")
      print("Veux tu continuer? (oui ou non)")
      reponse2 = input("Réponse: ")
      if reponse2 == "non":
            print("Au Revoir")
            quit()
    elif reponse =="3":
        print("La Réponse est fausse!")
        print("Veux tu continuer? (oui ou non)")
        reponse1 = input("Réponse: ")
        if reponse1 == "non":
            print("Au Revoir")
            quit()
        
  ga3 = input("bienvenue á la deuxieme Question! ENTER")
  rep2=True
  while(rep2):
    print("Tu est enfermé dans une Maison, Il y a trois portes pour sortir. Dans la première Porte il y a de la lave partout. Dans la deuzième Porte il y a un Lion qui a rien mange de puis un jour. Dans la troizième porte il y a des Brachiosaures! Quel porte prend tu?")
    print("1 La Lave")
    print("2 Le Lion")
    print("3 Les Brachiosaures")
    reponse = input("Réponse: ")
    if reponse == "3":
      print("La Réponse est Correct, Les Brachiosaures mange pas de Viandes!")
      rep2=False
    elif reponse == "2":
      print("La Réponse est fausse")
      print("Veux tu continuer? (oui ou non)")
      reponse1 = input("Réponse: ")
      if reponse1 == "non":
          print("Au Revoir")
          quit()
    elif reponse == "1":
      print("La Réponse est fausse")
      print("Veux tu continuer? (oui ou non)")
      reponse3 = input("Réponse: ")
      if reponse3 == "non":
          print("Au Revoir")
          quit()


  ga5 = input("Bienvenue à la troizième Question!")
  rep3 = True
  while(rep3):
    print("Tu est enfermé dans une petite Salle avec trois Portes. Dans la première Porte il y a du Feu. Dans la dans la deuxième Porte il y a un Lion qui a rien mangé depuis 4 ans. Dans la troizième Porte il y a du Gase qui te tue. Quel Porte prend tu?")
    print("1 Le Feu")
    print("2 Le Lion")
    print("3 Le Gase")
    reponse = input("Réponse: ")
    if reponse == "2":
      print("La Réponse est Correct, Le Lion n'a rien mangé depuis 4 ans il est dejà mort.")
      rep3 = False
    elif reponse =="1":
      print("La Réponse est fausse!")
      print("Veux tu continuer? (oui ou non)")
      reponse3 = input("Réponse: ")
      if reponse3 == "non":
          print("Au Revoir")
          quit()
    elif reponse =="3":
      print("La Réponse est fausse!")
      print("Veux tu continuer? (oui ou non)")
      reponse3 = input("Réponse: ")
      if reponse3 == "non":
          print("Au Revoir")
          quit()  
    
    print("Félicitations! Tu a fini le Quiz.")
    print("Veux tu recommencer oui ou non?")
    reponse = input("Réponse: ")
    if reponse =="oui":
      rep0 = False
    elif reponse =="non":
      print("Au Revoir")
      quit()