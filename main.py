    import string
    import random
     
    taille = random.randint(4, 12)
     
    lettres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(lettres) for l in range(taille))
     
    print(mot_de_passe)
     
    def verificateur_mdp(mdp):
        if len(mdp) >= 8 and any(l.isupper() for l in mdp) and len([n for n in mdp if n.isdigit()]) >= 2:
    	return True
        return False
     
    succes = verificateur_mdp(mot_de_passe)
    print(succes)