import random

mots = {
    "communiquer": "comunicar",
    "échanger": "intercambiar",
    "s’informer": "informarse",
    "dénoncer": "denunciar",
    "influencer": "influir",
    "publier": "publicar",
    "télecharger": "subir",
    "jouer": "jugar",
    "s’organiser": "organizarse",
    "chater": "chatear",
    "utilisateur": "usuario",
    "vitesse": "rapidez",
    "flux": "flujo",
    "rapide": "rapido",
    "puissant": "potente",
    "connecté": "conectado",
    "accorder de l’importance": "importar",
    "être accro": "estar engachado",
    "harceleur": "acosador",
    "confiance": "confianza",
    "piège": "trampa",
    "mensonge": "mentira",
    "tromper": "enganar",
    "prévenir": "avisar",
    "se méfier": "desconfiar",
    "menacer": "amenazar",
    "éduquer": "educar",
    "surveiller": "vigilar",
    "profil": "perfil",
    "écran": "pantalla"
}
faux=0
mots_restants = list(mots.keys())

def choisir_mot_aleatoire():
    return random.choice(mots_restants)

while mots_restants:
    mot_francais = choisir_mot_aleatoire()
    mot_espagnol = mots[mot_francais]
    
    reponse = input(f"Traduisez le mot '{mot_francais}' en espagnol : ")
    
    if reponse.lower() == mot_espagnol.lower():
        print("Correct !")
        mots_restants.remove(mot_francais)
    else:
        print(f"Incorrect. Le mot correct est '{mot_espagnol}'.")
        faux+=1
    print(f"Il vous reste {len(mots_restants)} mots à réviser.\n")

print("Félicitations ! Vous avez révisé tous les mots.")
print(f"Nombre de faux : {faux}")
