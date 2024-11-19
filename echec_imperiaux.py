import tkinter as tk
import tkinter.messagebox

class PreConfig:
    def __init__(self, default_n):
        self.root = tk.Tk()
        self.root.title("Configuration")
        self.n = tk.IntVar(value=default_n)
        
        label = tk.Label(self.root, text="Choisissez la dimension du plateau (pair, entre 6 et 12):")
        label.pack(pady=10)
        
        self.scale = tk.Scale(self.root, from_=6, to=12, orient=tk.HORIZONTAL, variable=self.n)
        self.scale.pack(pady=10)
        
        button = tk.Button(self.root, text="Valider", command=self.validate)
        button.pack(pady=10)
        
        self.root.mainloop()
    
    def validate(self):
        if self.n.get() % 2 == 0:
            self.root.destroy()
        else:
            tk.messagebox.showerror("Erreur", "La dimension doit être un nombre pair.")



class Joueur:
    coordonnees_reine = []
    nbr_pions = 0
    def __init__(self,coordonnees_reine,nbr_pions):
        self.coordonnees_reine = coordonnees_reine
        self.nbr_pions = nbr_pions

class Jeu:
    def __init__(self, n):
        self.n = n
        self.joueur = 1
        self.tableau = self.create_plateau()
        self.joueur1 =Joueur([0,n],n**2 // 4)
        self.joueur2 =Joueur([n,0],n**2 // 4)
        
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
    def possible(self,i,j):

        if self.joueur == 1 and (self.tableau[i][j].cget('bg') == "red3" or self.tableau[i][j].cget('bg') == "darkorange2"):
            return True
        elif self.joueur == 2 and ( self.tableau[i][j].cget('bg')=='blue3' or self.tableau[i][j].cget('bg')=='purple2') :
            return True
        else:
            return False

    def selectedpion(self, i, j):
        
        if self.possible(i,j):
            if self.joueur == 1:
                if self.tableau[i][j].cget('bg')== "darkorange2":
                    self.tableau[i][j].config(bg='darkorange4')
                    directions = [(-1, 0),(-1,-1), (1, 0), (1,1),(1,-1),(-1,1),(0, -1), (0, 1)]
                else:
                    self.tableau[i][j].config(bg='red3')
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            else:
                if self.tableau[i][j].cget('bg')== "purple2":
                    self.tableau[i][j].config(bg='purple4')
                    directions = [(-1, 0),(-1,-1) ,(1, 0), (1,1),(1,-1),(-1,1),(0, -1), (0, 1)]
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
        if self.joueur == 1:
            if self.tableau[ancieni][ancienj].cget('bg')== "darkorange4":
                    self.tableau[i][j].config(bg='darkorange2',command = lambda i=i, j=j: self.selectedpion(i,j))
            else:
                self.tableau[i][j].config(bg='red3',command = lambda i=i, j=j: self.selectedpion(i,j))
        else:
            if self.tableau[ancieni][ancienj].cget('bg')== "purple4":
                self.tableau[i][j].config(bg='purple2',command = lambda i=i, j=j: self.selectedpion(i,j))
            else:
                self.tableau[i][j].config(bg='blue3',command = lambda i=i, j=j: self.selectedpion(i,j))
        self.tableau[ancieni][ancienj].config(bg='white',command = lambda:self.inutile())

     
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau)):
                if self.tableau[i][j].cget('bg') =='red' or self.tableau[i][j].cget('bg') =='blue':
                    self.tableau[i][j].config(bg='white',command = lambda:self.inutile())
      
        if self.joueur == 1:
            self.joueur = 2
        else:
            self.joueur = 1
        self.label_joueur.config(text="Joueur: " + str(self.joueur))

    def inutile(self):
        return

if __name__ == "__main__":
    preconfig = PreConfig(8)
    jeu = Jeu(preconfig.n)
    jeu.UI()