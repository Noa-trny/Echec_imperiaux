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
    


    def move_reine(self, start, end):
                start_x, start_y = start
                end_x, end_y = end

                if start_x == end_x or start_y == end_y or abs(start_x - end_x) == abs(start_y - end_y):
                    step_x = (end_x - start_x) // max(1, abs(end_x - start_x))
                    step_y = (end_y - start_y) // max(1, abs(end_y - start_y))

                    x, y = start_x + step_x, start_y + step_y
                    while (x, y) != (end_x, end_y):
                        if self.plateau[x][y].cget('bg') != 'white':
                            return False
                        x += step_x
                        y += step_y

                    if self.plateau[end_x][end_y].cget('bg') == 'white':
                        self.plateau[start_x][start_y].config(bg='white')
                        self.plateau[end_x][end_y].config(bg='orange')
                        return True
                return False
    
    def move_pion(self, start, end):
                start_x, start_y = start
                end_x, end_y = end

                if start_x == end_x and self.plateau[end_x][end_y].cget('bg') == 'white' and end_y == start_y + 1:
                    self.plateau[start_x][start_y].config(bg='white')
                    self.plateau[end_x][end_y].config(bg='orange')
                    return True
                return False
    


    def deplacement(self):
        pass
        
    def pion_selectionne(self):
        if joueur.type_pion1:
            return joueur.type_pion1
        return joueur.type_pion2
    
    def nombre_pions(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.plateau[i][j].cget('bg') != 'white':
                    joueur.nbr_pions += 1
        return joueur.nbr_pions
    


    def deplacement_possibles(self):
        if joueur.type_pion1:
            def possible_reine(start):
                start_x, start_y = start
                for i in range(self.n):
                    for j in range(self.n):
                        if self.move_reine(start, (i, j)):
                            return True
                return False
        if joueur.type_pion2:
            def possible_pion(start):
                start_x, start_y = start
                if self.move_pion(start, (start_x + 1, start_y)):
                    return True
                return False

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
