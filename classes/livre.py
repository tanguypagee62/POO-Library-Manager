class Livre:
    # Classe représentant un livre dans la bibliothèque

    def __init__(self, titre, auteur, genre, isbn):
        # Constructeur de la classe Livre
        # Initialise le titre, l'auteur, le genre, et l'ISBN du livre
        # Par défaut, le livre n'est pas emprunté

        self.titre = titre         # Titre du livre
        self.auteur = auteur       # Auteur du livre
        self.genre = genre         # Genre du livre
        self.isbn = isbn           # Numéro ISBN du livre
        self.est_emprunte = False  # Statut d'emprunt, False signifie disponible

    def emprunter(self):
        # Méthode pour emprunter le livre
        # Si le livre n'est pas déjà emprunté, le statut change à emprunté
        # Sinon, un message indique que le livre est déjà emprunté

        if not self.est_emprunte:
            self.est_emprunte = True
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.titre}' est déjà emprunté.")

    def retourner(self):
        # Méthode pour retourner le livre
        # Si le livre est actuellement emprunté, le statut est modifié à disponible
        # Sinon, un message indique que le livre n'était pas emprunté

        if self.est_emprunte:
            self.est_emprunte = False
            print(f"Le livre '{self.titre}' a été retourné.")
        else:
            print(f"Le livre '{self.titre}' n'est pas emprunté actuellement.")

    def __str__(self):
        # Méthode spéciale pour obtenir une représentation textuelle de l'objet
        # Affiche le titre, l'auteur, le genre, et le statut du livre

        statut = "emprunté" if self.est_emprunte else "disponible"
        return f"{self.titre} par {self.auteur} ({self.genre}) - {statut}"
