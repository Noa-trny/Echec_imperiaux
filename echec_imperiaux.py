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
    
    def deplacer_reine(self, i, j):
        self.coordonnees_reine = [i, j]

    



class Jeu:
    def __init__(self, n):
        self.n = n
        self.plateau = [] 
        self.joueur1 = joueur([0,n-1], n**2 // 4)
        self.joueur2 = joueur([n-1,0], n**2 // 4)

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
    
    def UI(self):
        self.root = tk.Tk()
        self.root.title("Game")
        self.label_joueur = tk.Label(self.root, text="Joueur 1")
        self.label_joueur.grid(row=self.n, columnspan=self.n)
        self.label_nbr_pions = tk.Label(self.root, text="Nombre de pions : " + str(self.joueur1.nbr_pions))
        self.create_plateau()
        self.root.mainloop()


        
    def selectedpion(self, i, j):
    
        self.tableau[i][j].config(bg='green')

        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            k = 1
            while True:
                ni, nj = i + k * di, j + k * dj
            
                if 0 <= ni < self.n and 0 <= nj < self.n:
            
                    if self.tableau[ni][nj].cget("bg") == 'white':
                        self.tableau[ni][nj].config(bg='brown')
                        k += 1
                    else:
                        break  
                else:
                    break 

    def move(self,ancieni,ancienj,i,j):
        self.tableau[ancieni][ancienj].config(bg='white')
        self.tableau[i][j].config(bg='red')
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            k = 1
            while True:
                ni, nj = i + k * di, j + k * dj
            
                if 0 <= ni < self.n and 0 <= nj < self.n:
            
                    if self.tableau[ni][nj].cget("bg") == 'brown':
                        self.tableau[ni][nj].config(bg='white',command=lambda ancieni=i,ancienj=j,i=ni,j=nj: self.move(ancieni,ancienj,i,j))
                        k += 1
                    else:
                        break  
                else:
                    break 
    
    def nombre_pions(self,joueur):
        for i in range(self.n):
            for j in range(self.n):
                if self.plateau[i][j].cget('bg') != 'white':
                    joueur.nbr_pions += 1
        return joueur.nbr_pions
    



    def update(self):
        pass


    def possible(self):
        pass

    def again(self):
        return True
    
    def est_gagnant(self):
        if joueur.nbr_pions <= 3:
            return True

    


jeu = Jeu(10)
jeu.UI()
