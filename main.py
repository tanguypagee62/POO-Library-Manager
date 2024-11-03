import tkinter as tk
from tkinter import messagebox, simpledialog
from classes.livre import Livre
from classes.auteur import Auteur

class BibliothequeApp:
    # Classe principale de l'application de gestion de bibliothèque

    def __init__(self, root):
        # Initialisation de l'application
        # 'root' est la fenêtre principale de l'interface

        self.root = root
        self.root.title("Gestion de bibliothèque")

        # Listes pour stocker les instances de livres et d'auteurs
        self.livres = []
        self.auteurs = []

        # Création des widgets de l'interface
        self.create_widgets()

    def create_widgets(self):
        # Méthode pour créer et disposer les widgets sur l'interface

        # Label pour le titre de l'application
        tk.Label(self.root, text="Gestion de Bibliothèque", font=("Helvetica", 16)).pack(pady=10)

        # Bouton pour ajouter un livre, appelle la méthode 'ajouter_livres' quand on clique
        tk.Button(self.root, text="Ajouter un Livre", command=self.ajouter_livres).pack(pady=5)

        # Bouton pour afficher tous les livres, appelle la méthode 'afficher_livres' quand on clique
        tk.Button(self.root, text="Afficher les Livres", command=self.afficher_livres).pack(pady=5)

        # Bouton pour ajouter un auteur, appelle la méthode 'ajouter_auteurs' quand on clique
        tk.Button(self.root, text="Ajouter un Auteur", command=self.ajouter_auteurs).pack(pady=5)

        # Bouton pour afficher tous les auteurs, appelle la méthode 'afficher_auteurs' quand on clique
        tk.Button(self.root, text="Afficher les Auteurs", command=self.afficher_auteurs).pack(pady=5)

    def ajouter_livres(self):
        # Méthode pour ajouter un livre à la bibliothèque

        # Demande à l'utilisateur d'entrer les informations du livre
        titre = simpledialog.askstring("Titre", "Entrez le titre du livre :")
        auteur = simpledialog.askstring("Auteur", "Entrez l'auteur du livre :")
        genre = simpledialog.askstring("Genre", "Entrez le genre du livre :")
        isbn = simpledialog.askstring("ISBN", "Entrez l'ISBN du livre :")

        # Vérifie que tous les champs sont remplis, puis crée et ajoute le livre
        if titre and auteur and genre and isbn:
            livre = Livre(titre, auteur, genre, isbn)
            self.livres.append(livre)
            messagebox.showinfo("Succès", "Le livre a été ajouté avec succès.")
        else:
            messagebox.showinfo("Erreur", "Tous les champs doivent être remplis.")

    def afficher_livres(self):
        # Méthode pour afficher tous les livres de la bibliothèque

        if not self.livres:
            # Si aucun livre n'est dans la liste, affiche un message informatif
            messagebox.showinfo("Livres", "Aucun livre enregistré.")
            return
        
        # Crée une chaîne de caractères pour afficher chaque livre
        livres_str = "\n".join(str(livre) for livre in self.livres)
        messagebox.showinfo("Livres", livres_str)

    def ajouter_auteurs(self):
        # Méthode pour ajouter un auteur à la bibliothèque

        # Demande à l'utilisateur d'entrer le nom et le prénom de l'auteur
        nom = simpledialog.askstring("Nom", "Entrez le nom de l'auteur :")
        prenom = simpledialog.askstring("Prénom", "Entrez le prénom de l'auteur :")
        
        # Vérifie que tous les champs sont remplis, puis crée et ajoute l'auteur
        if nom and prenom:
            auteur = Auteur(nom, prenom)
            self.auteurs.append(auteur)
            messagebox.showinfo("Succès", "L'auteur a été ajouté avec succès.")
        else:
            messagebox.showinfo("Erreur", "Tous les champs doivent être remplis.")
    
    def afficher_auteurs(self):
        # Méthode pour afficher tous les auteurs de la bibliothèque

        if not self.auteurs:
            # Si aucun auteur n'est dans la liste, affiche un message informatif
            messagebox.showinfo("Auteurs", "Aucun auteur enregistré.")
            return
        
        # Crée une chaîne de caractères pour afficher chaque auteur
        auteurs_str = "\n".join(str(auteur) for auteur in self.auteurs)
        messagebox.showinfo("Auteurs", auteurs_str)

# Point d'entrée principal du programme
if __name__ == "__main__":
    # Crée la fenêtre principale Tkinter
    root = tk.Tk()
    
    # Instancie l'application de bibliothèque avec la fenêtre Tkinter
    app = BibliothequeApp(root)
    
    # Lance la boucle principale de l'interface
    root.mainloop()
