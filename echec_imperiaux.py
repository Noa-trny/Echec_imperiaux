import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as messagebox

class Joueur:
    def __init__(self, coordonnees_reine, nbr_pions):
        self.coordonnees_reine = coordonnees_reine
        self.nbr_pions = nbr_pions

class Jeu:
    COULEURS = {
        1: {'pion': 'red3', 'reine': 'darkorange2', 'case': 'red'},
        2: {'pion': 'blue3', 'reine': 'purple2', 'case': 'blue'}
    }

    def __init__(self):
        self.root = tk.Tk()
        self.n = self.choisir_taille_plateau()
        self.temp = 0
        self.joueur = 1
        self.tableau = None
        
        self.joueur1 = Joueur([0, self.n-1], self.n**2 // 4)
        self.joueur2 = Joueur([self.n-1, 0], self.n**2 // 4)

    def create_plateau(self):
        """Crée le plateau de jeu en fonction de la taille donnée."""
        tableau = []

        for i in range(self.n):
            row = []
            for j in range(self.n):
                if i == 0 and j == self.n - 1:
                    bg = self.COULEURS[1]['reine']
                elif i == self.n - 1 and j == 0:
                    bg = self.COULEURS[2]['reine']
                elif (i < self.n // 2 and j >= self.n // 2):
                    bg = self.COULEURS[1]['pion']
                elif (i >= self.n // 2 and j < self.n // 2):
                    bg = self.COULEURS[2]['pion']
                else:
                    bg = 'white'

                btn = tk.Button(self.root, bg=bg, width=4, height=2,
                                command=lambda i=i, j=j: self.selectedpion(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            tableau.append(row)

        # Affichage du joueur actif
        self.label_joueur = tk.Label(self.root, text="Joueur: " + str(self.joueur))
        self.label_joueur.grid(row=self.n, columnspan=self.n)
        
        return tableau

    def deselect_pion(self):
        """Désélectionne les pions et réinitialise les cases jouables."""
        for row in self.tableau:
            for btn in row:
                if btn.cget('bg') in [self.COULEURS[1]['case'], self.COULEURS[2]['case']]:
                    btn.config(bg='white', command=self.inutile)
                elif btn.cget('bg') in ['darkorange4', 'purple4']:
                    btn.config(bg=self.COULEURS[1]['reine'] if self.joueur == 1 else self.COULEURS[2]['reine'])

        self.temp = 0

    def mouvements_possibles(self, i, j, directions):
        """Retourne les cases jouables à partir des coordonnées (i, j)."""
        cases = []
        for di, dj in directions:
            k = 1
            while True:
                ni, nj = i + k * di, j + k * dj
                if 0 <= ni < self.n and 0 <= nj < self.n and self.tableau[ni][nj].cget('bg') == 'white':
                    cases.append((ni, nj))
                    k += 1
                else:
                    break
        return cases

    def selectedpion(self, i, j):
        """Gère la sélection et la mise en surbrillance des pions."""
        if self.temp >= 1:
            self.deselect_pion()

        if self.possible(i, j):
            self.temp += 1
            couleur = self.COULEURS[self.joueur]
            btn = self.tableau[i][j]

            if btn.cget('bg') == couleur['reine']:
                btn.config(bg='darkorange4' if self.joueur == 1 else 'purple4')
                directions = [(-1, 0), (-1, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (0, -1), (0, 1)]
            else:
                btn.config(bg=couleur['pion'])
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            cases_possibles = self.mouvements_possibles(i, j, directions)
            for ni, nj in cases_possibles:
                self.tableau[ni][nj].config(
                    bg=couleur['case'],
                    command=lambda ancieni=i, ancienj=j, i=ni, j=nj: self.move(ancieni, ancienj, i, j)
                )

    def move(self, ancieni, ancienj, i, j):
        """Effectue un mouvement et met à jour le plateau."""
        couleur = self.COULEURS[self.joueur]

        if self.tableau[ancieni][ancienj].cget('bg') in ['darkorange4', 'purple4']:
            self.tableau[i][j].config(bg=couleur['reine'], command=lambda i=i, j=j: self.selectedpion(i, j))
        else:
            self.tableau[i][j].config(bg=couleur['pion'], command=lambda i=i, j=j: self.selectedpion(i, j))

        self.tableau[ancieni][ancienj].config(bg='white', command=self.inutile)
        self.deselect_pion()
        self.prise(i, j)
        self.joueur = 2 if self.joueur == 1 else 1
        self.label_joueur.config(text="Joueur: " + str(self.joueur))

    def possible(self, i, j):
        """Vérifie si un pion peut être sélectionné."""
        couleur = self.COULEURS[self.joueur]
        return self.tableau[i][j].cget('bg') in [couleur['pion'], couleur['reine']]

    def prise(self, i, j):
        """Capture les pions adverses si possible."""
        couleur_adverse = self.COULEURS[2 if self.joueur == 1 else 1]
        reine = self.joueur1.coordonnees_reine if self.joueur == 1 else self.joueur2.coordonnees_reine

        # print(f"Vérification de prise pour la reine en {reine} et le pion en ({i}, {j})")

        if i != reine[0] and j != reine[1]:
            rect_sommets = [(reine[0], j), (i, reine[1])]
            for x, y in rect_sommets:
                # print(f"Vérification de la case ({x}, {y})...")
                if 0 <= x < self.n and 0 <= y < self.n:
                    bg_color = self.tableau[x][y].cget('bg')
                    # print(f"Couleur de la case : {bg_color}")
                    if bg_color == couleur_adverse['pion']:
                        # print(f"Pion capturé en ({x}, {y})")
                        self.tableau[x][y].config(bg='white', command=self.inutile)
                        if self.joueur == 1:
                            self.joueur2.nbr_pions -= 1
                        else:
                            self.joueur1.nbr_pions -= 1
        # else:
            # print("Pas de prise possible")
        self.gagne()

    def gagne(self):
        """Vérifie si un joueur a gagné et affiche une popup."""
        if self.joueur1.nbr_pions <= 2:
            gagnant = "Joueur 2"
            messagebox.showinfo("Fin de la partie", f"Le {gagnant} a gagné la partie ! 🎉")
            self.root.destroy()  # Ferme l'application après l'affichage
            return self.joueur1, "a gagné"
        elif self.joueur2.nbr_pions <= 2:
            gagnant = "Joueur 1"
            messagebox.showinfo("Fin de la partie", f"Le {gagnant} a gagné la partie ! 🎉")
            self.root.destroy()  # Ferme l'application après l'affichage
            return self.joueur2, "a gagné"
        return None
    

    def inutile(self):
        """Commande par défaut pour les cases inutiles."""
        return

    def choisir_taille_plateau(self):
        """Panneau pour choisir la taille du plateau."""
        boucle = False
        while boucle == False:
            self.root.withdraw()
            taille = simpledialog.askinteger(
                "Taille du Plateau",
                "Entrez la taille du plateau (nombre pair, entre 6 et 12 comrpis.) :",
                minvalue=6, maxvalue=12
            )
            if not taille or taille % 2 != 0:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre pair entre 6 et 12.")
                continue
            else:
                self.n = taille
                boucle = True
            self.root.deiconify()
            print("j'ai choisit la taille")
            return self.n 
            

    def UI(self):
        """Lance l'interface graphique."""
        self.choisir_taille_plateau()
        self.tableau = self.create_plateau()
        self.root.mainloop()

# Lance le jeu avec un panneau d'affichage pour choisir la taille
jeu = Jeu()
jeu.UI()
