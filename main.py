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


e1 = Employe("Alex", 1)
e2 = Employe("Jean", 2)
e3 = Employe("Thomas", 3)

v1 = Voiture("Toyota Corolla", "AA111")
v2 = Voiture("Honda Civic", "BB222")
v3 = Voiture("Ford Focus", "CC333")

print("\nInformations initiales")

e1.afficher_info()
e2.afficher_info()

v1.afficher_info()
v2.afficher_info()

print("\nAttribution des voitures")

e1.attribuer_voiture(v1)
e2.attribuer_voiture(v2)

e1.afficher_info()
e2.afficher_info()

print("\nRetrait de voiture")

e1.retirer_voiture()

e1.afficher_info()

print("\nTest attribution interdite")

e3.attribuer_voiture(v2)