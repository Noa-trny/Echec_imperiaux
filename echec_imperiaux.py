import tkinter as tk
from tkinter import messagebox

class joueur:
    coordonnees_reine = []
    nbr_pions = 0
    type_pion1 = "reine"
    type_pion2 = "pion"

    def __init__(self, coordonnees_reine, nbr_pions):
        self.coordonnees_reine = coordonnees_reine
        self.nbr_pions = nbr_pions



class Jeu:
    def __init__(self, n):
        self.n = n
        self.plateau = [] 

    def create_plateau(self):
        liste1 = []
        for i in range(self.n // 2):
            liste2 = []
            for j in range(self.n):
                if j >= self.n // 2:
                    if i == 0 and j == self.n-1:
                        btn = tk.Button(self.root, bg="orange", width=4, height=2)
                    else:
                        btn = tk.Button(self.root, bg="red", width=4, height=2)
                else:
                    btn = tk.Button(self.root, bg="white", width=4, height=2)
                btn.grid(row=i, column=j)
                liste2.append(btn)
            liste1.append(liste2)

        for i in range(self.n // 2, self.n):
            liste2 = []
            for j in range(self.n):
                if j < self.n // 2:
                    if i == self.n - 1 and j == 0:
                        btn = tk.Button(self.root, bg="purple", width=4, height=2)
                    else:
                        btn = tk.Button(self.root, bg="blue", width=4, height=2)
                else:
                    btn = tk.Button(self.root, bg="white", width=4, height=2)
                btn.grid(row=i, column=j)
                liste2.append(btn)
            liste1.append(liste2)

        return liste1

    def deplacement(self):
        pass

    def possible(self):
        pass

    def again(self):
        return True
    
    def est_gagnant(self):
        if joueur.nbr_pions <= 3:
            return True

    def UI(self):
        self.root = tk.Tk()
        self.root.title("Game")
        self.create_plateau()
        self.root.mainloop()

jeu = Jeu(10)
jeu.UI()
