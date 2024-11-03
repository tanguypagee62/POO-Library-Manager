class Auteur:
    # Classe représentant un auteur dans la bibliothèque

    def __init__(self, nom, prenom):
        # Constructeur de la classe Auteur
        # Initialise le nom et le prénom de l'auteur
        # Initialise une liste pour stocker les livres associés à cet auteur

        self.nom = nom              # Nom de famille de l'auteur
        self.prenom = prenom        # Prénom de l'auteur
        self.livres = []            # Liste pour stocker les livres écrits par cet auteur

    def ajouter_livre(self, livre):
        # Méthode pour ajouter un livre à la liste des livres de l'auteur
        # 'livre' doit être une instance de la classe Livre
        # Affiche un message de confirmation

        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté à l'auteur {self.nom} {self.prenom}.")

    def __str__(self):
        # Méthode spéciale pour obtenir une représentation textuelle de l'objet Auteur
        # Affiche le prénom, le nom de l'auteur, et le nombre de livres écrits

        return f"{self.prenom} {self.nom} - {len(self.livres)} livre(s) écrit(s)."
