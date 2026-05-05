# 🦍 Donkey Kong – Projet NSI

> Projet de fin d'année – Classe 103 | 2025-2026
> Trinôme : **Sami** · **Raphaël** · **Quentin**

---

## 📋 Description

Jeu de plateforme inspiré de l'arcade **Donkey Kong** (1981), développé en Python avec la bibliothèque Pygame dans le cadre du cours de **NSI (Numérique et Sciences Informatiques)**.

Aide **Mario** à sauver **Pauline** kidnappée par Donkey Kong en grimpant jusqu'en haut de la structure tout en évitant les tonneaux !

---

## 🎮 Comment jouer

| Touche | Action |
|---|---|
| ⬅️ Flèche gauche | Déplacer Mario à gauche |
| ➡️ Flèche droite | Déplacer Mario à droite |
| ⬆️ Flèche haut | Monter une échelle |
| ⬇️ Flèche bas | Descendre une échelle |
| `ESPACE` | Sauter (seul ou en combinaison avec ←/→) |
| `ENTRÉE` | Valider un choix dans les menus |
| `ÉCHAP` | Quitter le jeu |

### 🏆 Objectif
- Atteins **le haut de la structure** pour sauver Pauline
- Sauve-la **5 fois** OU atteins un score de **999 999** pour gagner la partie

### 💀 Règles
- Tu disposes de **3 vies**
- Un tonneau touché = **une vie perdue**
- **+100 points** en sautant par-dessus un tonneau
- **+250 points** en sauvant Pauline à chaque niveau

---

## 🛠️ Installation

### Prérequis — Python 3.8+

Vérifie que Python est installé :
```bash
python3 --version
```

Si ce n'est pas le cas, télécharge-le sur **[python.org](https://www.python.org/downloads/)**.

> ✅ Compatible **Windows**, **macOS** et **Linux**

---

### Étape 1 — Cloner le projet

```bash
git clone https://github.com/120480986kf-alt/DonkeyKong
cd DonkeyKong-1
```

Ou télécharge le ZIP depuis le bouton vert **`Code`** en haut de la page, puis décompresse-le.

---

### Étape 2 — Installer les dépendances

```bash
pip3 install -r requirements.txt
```

> Si `pip3` ne fonctionne pas, essaie `python3 -m pip install -r requirements.txt`

---

## 🚀 Lancer le jeu

```bash
python3 DonkeyKong_NDO.py
```

### Depuis un éditeur de code

| Éditeur | Comment lancer |
|---|---|
| **VS Code** | Ouvre le fichier → clique sur ▶️ en haut à droite |
| **PyCharm** | Ouvre le fichier → `Shift + F10` ou bouton ▶️ |
| **IDLE** | `Run > Run Module` ou appuie sur `F5` |

---

## 📁 Structure du projet

```
DonkeyKong-1/
│
├── DonkeyKong_NDO.py         ← Code source principal
├── requirements.txt          ← Dépendances Python
├── README.md                 ← Ce fichier
│
└── assets/                   ← Toutes les ressources graphiques
    ├── title-screen.png      ← Écran titre
    ├── start.png             ← Écran de démarrage
    ├── win-screen.png        ← Écran de victoire
    ├── game-over-screen.png  ← Écran Game Over
    ├── level.png             ← Décor du niveau
    ├── mario-*.png           ← Sprites de Mario
    ├── DK_*.png / dk*.png    ← Sprites de Donkey Kong
    ├── pauline-*.png         ← Sprites de Pauline
    ├── barrel*.png           ← Sprites des tonneaux
    ├── platform*.png         ← Sprites des plateformes
    └── ...                   ← Autres ressources
```

---

## ❓ Problèmes fréquents

| Erreur | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'pygame'` | Relance `pip3 install -r requirements.txt` |
| `FileNotFoundError: ... assets/...png` | Vérifie que le dossier `assets/` est bien présent à côté du `.py` |
| Fenêtre noire au lancement | Vérifie que tous les fichiers dans `assets/` sont bien présents |
| Pygame installé mais jeu ne démarre pas | Essaie `python3 -m pygame.examples.aliens` pour tester pygame |

---

## 🧠 Concepts informatiques utilisés

- Boucle de jeu principale (`while`)
- Conditions et booléens
- Fonctions avec paramètres et valeurs de retour
- Listes et indices
- Génération aléatoire (`random`)
- Gestion des collisions (coordonnées x/y)
- Gestion des événements clavier
- Sprites et animations
- États du jeu (menu, intro, jeu, fin)

---

## 👥 Répartition du travail

| Rôle | Membre |
|---|---|
| Chef de projet – coordination, présentation | Quentin |
| Développeur – code, logique, corrections | Sami |
| Designer / Testeur – visuels, tests | Raphaël |

---

## 📚 Ressources

- [Documentation Pygame](https://www.pygame.org/docs/)
- [Python.org](https://www.python.org/)
- Jeu original : *Donkey Kong* – Nintendo, 1981

---

*Projet réalisé dans le cadre du cours NSI – Lycée NDO, 2025-2026*
