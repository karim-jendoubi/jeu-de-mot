mot = "secret"
motc = list("******")  # Utilisation d'une liste pour pouvoir modifier les caractères
essais = 20

print("Devinez le mot secret ! Vous avez 20 essais.")

for b in range(essais):
    lettre = input("Proposez une lettre : ").lower()  # Conversion en minuscule pour uniformiser
    trouve = False  # Variable pour suivre si une lettre a été trouvée

    for i in range(len(mot)):
        if mot[i] == lettre and motc[i] == '*':  
            motc[i] = lettre
            trouve = True

    # Affichage du mot partiellement deviné
    print("Mot actuel : " + "".join(motc))
    
    if not trouve:
        print("Cette lettre n'est pas dans le mot.")

    # Vérification de la victoire
    if "".join(motc) == mot:
        print("🎉 Bravo, vous avez trouvé le mot !")
        break
else:
    # Si l'utilisateur n'a pas trouvé après toutes les tentatives
    print(f"❌ Désolé, vous avez perdu. Le mot était '{mot}'.")
