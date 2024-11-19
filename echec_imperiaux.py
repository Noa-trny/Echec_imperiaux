import tkinter as tk

class Jeu:
    def __init__(self, n, joueur):
        self.n = n
        self.joueur = joueur
        self.tableau = self.create_plateau()
        
    def create_plateau(self):
        self.root = tk.Tk()
        liste1 = []  
        for i in range(self.n // 2):  
            liste2 = []  
            for j in range(self.n):
                if j >= self.n // 2:
                    if i == 0 and j == self.n-1:
                        btn = tk.Button(self.root, bg="darkorange2", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
                    else:
                        btn = tk.Button(self.root, bg="red3", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
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
                        btn = tk.Button(self.root, bg="purple2", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
                    else:
                        btn = tk.Button(self.root, bg="blue3", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
                else:
                    btn = tk.Button(self.root, bg="white", width=4, height=2)
                btn.grid(row=i, column=j)
                liste2.append(btn)
            liste1.append(liste2)

        return liste1

    def UI(self):
        self.root.title("Game")
        self.tableau

        self.label_joueur = tk.Label(self.root, text="Joueur: " + str(self.joueur))
        self.label_joueur.grid(row=self.n, columnspan=self.n)
        
        self.root.mainloop()

    def selectedpion(self, i, j):
        if self.joueur == 1:
            self.tableau[i][j].config(bg='red3')
        else:
            self.tableau[i][j].config(bg='blue4')

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            k = 1
            while True:
                ni, nj = i + k * di, j + k * dj
            
                if 0 <= ni < self.n and 0 <= nj < self.n:
                    if self.tableau[ni][nj].cget("bg") == 'white':
                        if self.joueur == 1:
                            self.tableau[ni][nj].config(bg='red', command=lambda ancieni=i, ancienj=j, i=ni, j=nj: self.move(ancieni, ancienj, i, j))
                        else:
                             self.tableau[ni][nj].config(bg='blue', command=lambda ancieni=i, ancienj=j, i=ni, j=nj: self.move(ancieni, ancienj, i, j))
                        k += 1
                    else:
                        break  
                else:
                    break 

    def move(self, ancieni, ancienj, i, j):
       
        self.tableau[ancieni][ancienj].config(bg='white')

      
        if self.joueur == 1:
            self.tableau[i][j].config(bg='red3')
        else:
            self.tableau[i][j].config(bg='blue4')

     
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau)):
                if self.tableau[i][j].cget('bg') =='red' or self.tableau[i][j].cget('bg') =='blue':
                    self.tableau[i][j].config(bg='white')
      
        if self.joueur == 1:
            self.joueur = 2
        else:
            self.joueur = 1



jeu = Jeu(8, 1)
jeu.UI()
