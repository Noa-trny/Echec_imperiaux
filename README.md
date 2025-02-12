# Jeu de Pions

## Description

Ce projet est un jeu de pions développé en Python utilisant la bibliothèque Tkinter pour l'interface graphique. Le jeu permet à deux joueurs de déplacer leurs pions sur un plateau, avec des règles simples de capture.

## Règles du Jeu

Deux joueurs s'affrontent sur un plateau carré comportant `n` lignes et `n` colonnes, où `n` est un entier pair. Par défaut, `n=8`.

Chaque joueur dispose de deux types de pièces :

- **Reine** : se déplace orthogonalement ou en diagonale vers une case vide non nécessairement adjacente, à condition que toutes les cases alignées entre sa position de départ et sa position d'arrivée soient vides.
- **Tour** : se déplace orthogonalement vers une case vide non nécessairement adjacente, à condition que toutes les cases alignées entre sa position de départ et sa position d'arrivée soient vides.

Chaque joueur possède initialement une reine et `n^2//4−1` tours disposées comme suit (le premier joueur a ici les pièces de couleur bleue et mauve et le second de couleur rouge et orange).

### Déplacements et Captures

- Après qu'un joueur ait déplacé l'une de ses tours, des captures sont possibles. Si la position finale de la tour n'est ni sur la même ligne ni sur la même colonne que la reine du même joueur, ces deux pièces forment deux sommets d'une même diagonale d'un rectangle virtuel. Si une ou deux tours du joueur adverse sont situées sur un ou deux des autres sommets de ce rectangle, elles sont capturées.
- Cette règle de capture ne s'applique qu'après le déplacement d'une tour et non d'une reine, et seules les tours adverses peuvent être capturées, pas la reine adverse.

### Fin de Partie

Dès qu'un joueur n'a plus que deux pièces ou moins (au cumul de sa reine et de ses tours), il a perdu la partie.

## Fonctionnalités

- Interface graphique intuitive avec Tkinter.
- Deux joueurs peuvent jouer l'un contre l'autre.
- Les pions peuvent être déplacés sur le plateau.
- Les pions capturés sont retirés du plateau.

## Installation

Pour exécuter ce projet, vous devez avoir Python installé sur votre machine. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/).

### Étapes d'installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Noa-trny/Echec_imperiaux.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd Echec_imperiaux
   ```
3. Exécutez le script principal :
   ```bash
   python echec_imperiaux.py
   ```

## Utilisation

1. Lancez le jeu en exécutant le script `echec_imperiaux.py`.
2. Suivez les instructions à l'écran pour déplacer vos pions.
3. Le jeu alterne entre les deux joueurs.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre ces étapes :

1. Forkez le projet.
2. Créez une nouvelle branche (`git checkout -b feature/YourFeature`).
3. Apportez vos modifications et validez (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez vos modifications (`git push origin feature/YourFeature`).
5. Ouvrez une Pull Request.

## Auteurs

- [Noa Tournoy](https://github.com/Noa-trny)
- [Noah Tournant](https://github.com/noah-tournant)

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
