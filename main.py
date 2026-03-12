class Employe:

    def __init__(self, nom, id_employe):
        self.nom = nom
        self.id_employe = id_employe
        self.voiture = None

    def afficher_info(self):
        if self.voiture:
            print(f"Employé: {self.nom} - Voiture: {self.voiture.modele}")
        else:
            print(f"Employé: {self.nom} - Aucune voiture assignée")

    def attribuer_voiture(self, voiture):

        if self.voiture is not None:
            print("Cet employé possède déjà une voiture")
            return

        if voiture.employe is not None:
            print("Cette voiture est déjà attribuée")
            return

        self.voiture = voiture
        voiture.employe = self

    def retirer_voiture(self):

        if self.voiture is None:
            print("Cet employé n'a pas de voiture")
            return

        self.voiture.employe = None
        self.voiture = None

class Voiture:

    def __init__(self, modele, immatriculation):
        self.modele = modele
        self.immatriculation = immatriculation
        self.employe = None

    def afficher_info(self):

        if self.employe:
            print(f"Voiture {self.modele} - Assignée à {self.employe.nom}")
        else:
            print(f"Voiture {self.modele} - Non assignée")