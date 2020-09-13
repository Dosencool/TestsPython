import random

points = 0
solution = random.randint(1, 100)
pastrouve = True
while(pastrouve):
    print("Devine un nombre de 1 à 100")
    reponseString = input("Réponse: ")
    reponse=0
    try:
        reponse=int(reponseString)                
    except ValueError:
        print("Tu dois mettre un nombre")        
        continue
    if reponse == 1183:
        print(solution)
    elif reponse == solution:
        print("Felicitations, tu as trouvé la solution!")
        print("Tu as pris "+points+" avant que tu as trouvé le bon numéro!")
        pastrouve = False
    elif reponse > solution:
        print("Ta réponse est trop grande!")
        points = +1
    elif reponse < solution:
        print("Ta réponse est trop petite")
        points = +1