import tkinter as tk

class Jeu:
    def __init__(self, n):
        self.n = n
        self.tableau = self.create_plateau()
        
    def create_plateau(self):
        self.root = tk.Tk()
        liste1 = []  
        for i in range(self.n // 2):  
            liste2 = []  
            for j in range(self.n):
                if j >= self.n // 2:
                    if i == 0 and j == self.n-1:
                        btn = tk.Button(self.root, bg="orange", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
                    else:
                        btn = tk.Button(self.root, bg="red", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
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
                        btn = tk.Button(self.root, bg="purple", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
                    else:
                        btn = tk.Button(self.root, bg="blue", width=4, height=2, command=lambda i=i, j=j: self.selectedpion(i,j))
                else:
                    btn = tk.Button(self.root, bg="white", width=4, height=2)
                btn.grid(row=i, column=j)
                liste2.append(btn)
            liste1.append(liste2)

        return liste1

    def UI(self):
        self.root.title("Game")
        self.tableau

        self.label_joueur = tk.Label(self.root, text="Joueur 1")
        self.label_joueur.grid(row=self.n, columnspan=self.n)
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

    def move(self,i,j):
        pass
        

jeu = Jeu(8)
jeu.UI()

