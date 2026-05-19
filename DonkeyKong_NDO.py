# ============================================================
# Trinôme  : Sami, Raphaël, Quentin
# Projet   : NSI – Jeu Donkey Kong
# Classe   : 103  |  Année : 2025-2026
# Description : Jeu de plateforme inspiré de l'arcade Donkey Kong
# ============================================================

# --- Importations des bibliothèques ---
import pygame, sys, os
from pygame.locals import *
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Définition des couleurs (Rouge, Vert, Bleu) ---
NOIR    = (0, 0, 0)
VERT    = (0, 255, 0)
ROUGE   = (255, 0, 0)
BLEU    = (0, 200, 255)
JAUNE   = (255, 255, 0)
VIOLET  = (170, 0, 225)
couleurs = [VERT, ROUGE, BLEU, JAUNE, VIOLET]

# --- Déclaration des variables globales ---
score        = 0
meilleurScore = 0      # Meilleur score de la session
numNiveau    = 0
diff         = 0       # Difficulté : augmente à chaque niveau

# --- États du jeu (booléens) ---
rejouer          = True
appuye           = False   # ESPACE pressé pour démarrer
monteFini        = False   # DK a fini de grimper (intro)
introFinie       = False   # Animation d'intro terminée
debutFait        = False   # Écran de démarrage affiché
afficheDebut     = False   # Déclencheur d'affichage du démarrage
jeuLance         = False   # Partie en cours
lanceTonneau     = False   # DK est en train de lancer un tonneau
sautGauche       = False   # Mario saute vers la gauche
sautDroite       = False   # Mario saute vers la droite
sautPlace        = False   # Mario saute sur place
touche           = False   # Mario a été touché par un tonneau
sceneMort        = False   # Scène de mort en cours
partieFinie      = False   # Game Over
victoireJeu      = False   # Le joueur a gagné la partie
victoireNiveau   = False   # Le joueur a gagné ce niveau
scoreMax         = False   # Score maximum atteint
sceneVicAff      = False   # Affichage scène de victoire finale
sceneVicFinie    = False   # Scène de victoire terminée

choix = "haut"             # Option sélectionnée dans les menus
sens  = "droite"           # Direction de déplacement de Mario

# --- Données des plateformes (animation intro) ---
platX  = [55, 55, 51, 60, 56, 56, 56]
platY  = [9, 10, 8, 9, 11, 9, 9, 11]
numPlat = 0

# --- Variables pour l'animation de Donkey Kong ---
dkMonte    = 0
vitMonte   = 15    # Vitesse de montée de DK
numPlat    = 0
dkSautX    = 378
dkSautY    = 172
dkSautDir  = 0     # Direction verticale du saut de DK

# --- Variables de Mario ---
mX       = 150     # Position x de Mario
mY       = 720     # Position y de Mario
forceSaut = -7     # Force initiale du saut
cptSaut  = 0       # Compteur de frames pendant le saut
ptSaut   = 0       # Point bonus si tonneau sauté
cptMort  = 0       # Compteur de frames pendant la mort
vies     = 2       # Nombre de vies

# --- Variables des tonneaux ---
tonX        = []   # Positions x de chaque tonneau
tonY        = []   # Positions y de chaque tonneau
cptLance    = 0    # Compteur avant lancer d'un tonneau
tonSens     = []   # Direction de chaque tonneau
chute       = []   # Tonneau en train de tomber (bool)
cptChute    = []   # Compteur de frames de chute
tonGauche   = []   # Tonneau peut aller à gauche (bool)
tonDroite   = []   # Tonneau peut aller à droite (bool)

# --- Points d'inclinaison des plateformes ---
pentesX     = [100, 140, 190, 240, 280, 330, 380, 430, 480, 530, 570, 620, 670, 720]
cptPente    = 0    # Nombre de pentes franchies pendant un saut

# --- Coordonnées des échelles (x début/fin, y haut/bas) ---
echX1 = [295, 605, 295, 345, 345, 150, 245, 385, 600, 600, 245, 150, 265, 265, 315, 555, 555, 600, 440, 320]
echX2 = [305, 610, 310, 350, 350, 160, 255, 400, 610, 610, 255, 160, 280, 280, 325, 565, 565, 610, 450, 335]
echY1 = [710, 635, 617, 610, 526, 538, 522, 423, 506, 435, 414, 338, 409, 332, 309, 314, 417, 241, 154, 232]
echY2 = [720, 705, 657, 620, 571, 608, 532, 523, 511, 475, 464, 408, 414, 382, 329, 369, 432, 311, 232, 272]
echHautOk = [False, True, True, False, True, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True]
echBasOk  = [True, True, False, True, False, True, True, True, True, False, False, True, True, False, True, False, True, True, True, False]

# --- Limites de déplacement gauche/droite ---
bornGaucheY = [541, 341]
bornDroiteY = [638, 438, 244]

# --- Données des confettis (animation de victoire) ---
confX    = []
confY    = []
confRayon = []
confVit  = []
confCoul = []

# --- Chargement de toutes les images du jeu ---
imgTitre    = pygame.image.load("assets/title-screen.png")
imgDebut    = pygame.image.load("assets/start.png")
imgVictoire = pygame.image.load("assets/win-screen.png")
imgGameOver = pygame.image.load("assets/game-over-screen.png")

imgCurseur  = pygame.image.load("assets/select-icon.png")
imgVie      = pygame.image.load("assets/mario-life.png")

imgAvecEch  = pygame.image.load("assets/withLadder.png")
plat0 = pygame.image.load("assets/platform0.png")
plat1 = pygame.image.load("assets/platform1.png")
plat2 = pygame.image.load("assets/platform2.png")
plat3 = pygame.image.load("assets/platform3.png")
plat4 = pygame.image.load("assets/platform4.png")
plat5 = pygame.image.load("assets/platform5.png")
plat6 = pygame.image.load("assets/platform6.png")
plateformes = [plat0, plat1, plat2, plat3, plat4, plat5, plat6]
imgNiveau   = pygame.image.load("assets/level.png")

# Chiffres bleus (numéro de niveau)
bleu0 = pygame.image.load("assets/blue0.png")
bleu1 = pygame.image.load("assets/blue1.png")
bleu2 = pygame.image.load("assets/blue2.png")
bleu3 = pygame.image.load("assets/blue3.png")
bleu4 = pygame.image.load("assets/blue4.png")
bleu5 = pygame.image.load("assets/blue5.png")
chiffresBleus = [bleu0, bleu1, bleu2, bleu3, bleu4, bleu5]

# Chiffres blancs (score)
blanc0 = pygame.image.load("assets/white0.png")
blanc1 = pygame.image.load("assets/white1.png")
blanc2 = pygame.image.load("assets/white2.png")
blanc3 = pygame.image.load("assets/white3.png")
blanc4 = pygame.image.load("assets/white4.png")
blanc5 = pygame.image.load("assets/white5.png")
blanc6 = pygame.image.load("assets/white6.png")
blanc7 = pygame.image.load("assets/white7.png")
blanc8 = pygame.image.load("assets/white8.png")
blanc9 = pygame.image.load("assets/white9.png")
chiffresBlancs = [blanc0, blanc1, blanc2, blanc3, blanc4, blanc5, blanc6, blanc7, blanc8, blanc9]

# Sprites de Mario (déplacement, saut, escalade, mort)
mGauche  = pygame.image.load("assets/mario-left.png")
mDroite  = pygame.image.load("assets/mario-right.png")
mCourseG = pygame.image.load("assets/run-left.png")
mCourseD = pygame.image.load("assets/run-right.png")
mSautG   = pygame.image.load("assets/jump-left.png")
mSautD   = pygame.image.load("assets/jump-right.png")
mEchelle1 = pygame.image.load("assets/marioClimb1.png")
mEchelle2 = pygame.image.load("assets/marioClimb2.png")
mMort     = pygame.image.load("assets/dead.png")
imgMario  = mDroite     # Image courante de Mario

# Sprites de Pauline
paulineAide  = pygame.image.load("assets/pauline-help.png")
paulineCalme = pygame.image.load("assets/pauline-still.png")

# Sprites de Donkey Kong
dkMonte1  = pygame.image.load("assets/DK_up1.png")
dkMonte2  = pygame.image.load("assets/DK_up2.png")
dkVide1   = pygame.image.load("assets/dkClimbEmpty1.png")
dkVide2   = pygame.image.load("assets/dkClimbEmpty2.png")
dkFace    = pygame.image.load("assets/dkForward.png")
dkGauche  = pygame.image.load("assets/dkLeft.png")
dkDroite  = pygame.image.load("assets/dkRight.png")
dkDefaite = pygame.image.load("assets/dk-defeat.png")
imgDK     = dkFace      # Image courante de DK

# Sprites des tonneaux
pileTon  = pygame.image.load("assets/barrel-stack.png")
ton1     = pygame.image.load("assets/barrel1.png")
ton2     = pygame.image.load("assets/barrel2.png")
ton3     = pygame.image.load("assets/barrel3.png")
ton4     = pygame.image.load("assets/barrel4.png")
seqTon   = [ton1, ton2, ton3, ton4]   # Séquence d'animation du tonneau
imgTon   = []                          # Image courante de chaque tonneau

# Images des cœurs (vies)
coeurBrise = pygame.image.load("assets/broken-heart.png")
coeurPlein = pygame.image.load("assets/full-heart.png")

# --- Initialisation aléatoire des 400 confettis ---
for i in range(0, 400):
    x = random.randint(0, 800)          # Position x aléatoire
    confX.append(x)

    y = random.randint(-500, -100)      # Position y hors écran (au-dessus)
    confY.append(y)

    r = random.randint(1, 4)            # Rayon aléatoire
    confRayon.append(r)

    v = random.randint(5, 20)           # Vitesse de chute aléatoire
    confVit.append(v)

    c = random.randint(0, 4)            # Couleur aléatoire
    confCoul.append(couleurs[c])


# ============================================================
# afficher_instructions - affiche les règles du jeu en console
# Paramètres : aucun | Retour : aucun
# ============================================================
def afficher_instructions():
    print("Donkey Kong a kidnappé Pauline !")
    print("Aide Mario à la sauver en grimpant jusqu'en haut de la structure.")
    print()
    print("Tu as 3 vies. Tu gagnes des points en sauvant Pauline")
    print("et en sautant par-dessus les tonneaux.")
    print("Pour gagner : sauve-la 5 fois OU atteins 999999 points.")
    print()
    print("Touches : flèches directionnelles pour se déplacer,")
    print("          ESPACE pour sauter.")
    print()
    print("Dans les menus : flèches HAUT/BAS pour choisir, ENTRÉE pour valider.")
    print()
    print("BONNE CHANCE !")
    print()


# ============================================================
# collision - vérifie si Mario a percuté un tonneau
# Paramètres : aucun | Retour : touche (bool)
# ============================================================
def collision():
    global touche

    for i in range(0, len(tonX)):
        # Collision si les sprites de Mario et du tonneau se chevauchent
        if mX+20 >= tonX[i] and mX <= tonX[i]+26 and mY+30 >= tonY[i] and mY <= tonY[i]+20:
            touche = True

    return touche


# ============================================================
# verif_echelle - vérifie si Mario est sur une échelle
# Paramètres : aucun | Retour : monter (bool), descendre (bool), bougerCotes (bool)
# ============================================================
def verif_echelle():
    global mY

    monter      = False
    descendre   = False
    bougerCotes = True

    for i in range(0, len(echX1)):
        # Mario est dans la zone d'une échelle
        if mX >= echX1[i] and mX <= echX2[i] and mY >= echY1[i] and mY <= echY2[i]:
            descendre   = True
            monter      = True
            bougerCotes = False

            # En haut de l'échelle : plus possible de monter
            if mY == echY1[i]:
                monter = False
                if echHautOk[i]:    # Échelle non brisée en haut
                    bougerCotes = True

            # En bas de l'échelle : plus possible de descendre
            if mY == echY2[i]:
                descendre = False
                if echBasOk[i]:     # Échelle non brisée en bas
                    bougerCotes = True

        # On sort dès qu'on a trouvé l'échelle de Mario
        if monter or descendre:
            break

    return monter, descendre, bougerCotes


# ============================================================
# pente - ajuste la position verticale selon l'inclinaison
# Paramètres : y (int), x (int), sens (str), objet (str)
# Retour : y (int) ou mvt (int)
# ============================================================
def pente(y, x, sens, objet):
    global cptPente

    # Détermine la plateforme et les paramètres de pente
    if y <= 720 and y >= 657:                                    # Plateforme du bas
        debut = 6;  fin = len(pentesX) - 1;  mvt = 3

    elif (y <= 638 and y >= 553) or (y >= 353 and y <= 438):    # 2e ou 4e plateforme
        debut = 0;  fin = len(pentesX) - 2;  mvt = -3

    elif (y <= 541 and y >= 456) or (y <= 341 and y >= 256):    # 3e ou 5e plateforme
        debut = 1;  fin = len(pentesX) - 1;  mvt = 3

    elif y <= 245 and y >= 149:                                  # Plateforme du haut
        debut = 8;  fin = len(pentesX) - 2;  mvt = -3

    else:                                                         # Sur une échelle
        debut = 0;  fin = 0;  mvt = 0

    # Applique la pente à chaque point d'inclinaison
    for i in range(debut, fin):
        if x == pentesX[i]:
            if (sautGauche or sautDroite) and objet == "mario":
                cptPente = cptPente + 1    # Compte les pentes sautées
            else:
                if sens == "droite":
                    y = y - mvt            # Monte en allant à droite
                elif sens == "gauche":
                    y = y + mvt            # Descend en allant à gauche

    if (sautGauche or sautDroite) and objet == "mario":
        return mvt
    else:
        return y


# ============================================================
# limites - vérifie si Mario ou un tonneau a atteint un bord
# Paramètres : x (int), y (int) | Retour : gauche (bool), droite (bool)
# ============================================================
def limites(x, y):
    gauche = True
    droite = True

    # Vérifie la limite gauche
    if x <= 105 and x >= 96:
        for i in range(0, len(bornGaucheY)):
            if y <= bornGaucheY[i] and y >= bornGaucheY[i] - 49:
                gauche = False

    # Vérifie la limite droite
    elif x >= 660 and x <= 669:
        for i in range(0, len(bornDroiteY)):
            if y <= bornDroiteY[i] and y >= bornDroiteY[i] - 49:
                droite = False

    return gauche, droite


# ============================================================
# scene_intro - animation : DK grimpe avec Pauline jusqu'en haut
# Paramètres : aucun | Retour : aucun
# ============================================================
def scene_intro():
    if dkMonte <= 390:
        # Fond avec échelle visible pendant la montée
        ecran.blit(imgAvecEch, (48, 0))
        if dkMonte % 30 == 0:
            ecran.blit(dkMonte2, (350, 660-dkMonte))
        else:
            ecran.blit(dkMonte1, (370, 660-dkMonte))

    elif dkMonte > 390 and dkMonte <= 580:
        # DK est en haut de l'échelle
        ecran.blit(plat0, (55, 9))
        ecran.blit(dkMonte2, (350, 660-dkMonte))

    if monteFini:
        # Plateformes qui tombent, Pauline apparaît, DK saute
        ecran.blit(plateformes[numPlat], (platX[numPlat], platY[numPlat]))
        afficher_pauline(paulineCalme)
        ecran.blit(dkFace, (dkSautX, dkSautY))


# ============================================================
# ecran_debut - affiche l'écran de démarrage du niveau
# Paramètres : aucun | Retour : aucun
# ============================================================
def ecran_debut():
    ecran.blit(imgDebut, (48, 0))


# ============================================================
# decor - affiche le fond du niveau et la pile de tonneaux
# Paramètres : aucun | Retour : aucun
# ============================================================
def decor():
    ecran.blit(imgNiveau, (31, -14))
    ecran.blit(pileTon, (60, 188))


# ============================================================
# afficher_dk - dessine Donkey Kong à l'écran
# Paramètres : aucun | Retour : aucun
# ============================================================
def afficher_dk():
    ecran.blit(imgDK, (130, 176))


# ============================================================
# afficher_mario - dessine Mario à sa position courante
# Paramètres : aucun | Retour : aucun
# ============================================================
def afficher_mario():
    ecran.blit(imgMario, (mX, mY))


# ============================================================
# afficher_pauline - dessine Pauline à l'écran
# Paramètres : img (image) | Retour : aucun
# ============================================================
def afficher_pauline(img):
    ecran.blit(img, (335, 133))


# ============================================================
# afficher_tonneaux - dessine tous les tonneaux actifs
# Paramètres : aucun | Retour : aucun
# ============================================================
def afficher_tonneaux():
    for i in range(0, len(imgTon)):
        ecran.blit(imgTon[i], (tonX[i], tonY[i]))


# ============================================================
# afficher_vies - dessine les icônes de vies restantes
# Paramètres : aucun | Retour : aucun
# ============================================================
def afficher_vies():
    for i in range(0, vies):
        ecran.blit(imgVie, (60+i*20, 100))


# ============================================================
# afficher_niveau - dessine le numéro du niveau courant
# Paramètres : aucun | Retour : aucun
# ============================================================
def afficher_niveau():
    for i in range(0, len(chiffresBleus)):
        if numNiveau / 10 == i:
            ecran.blit(chiffresBleus[i], (611, 86))
        if numNiveau % 10 == i:
            ecran.blit(chiffresBleus[i], (635, 86))


# ============================================================
# afficher_score - dessine un score sur 6 chiffres à l'écran
# Paramètres : val (int), x (int), y (int) | Retour : aucun
# ============================================================
def afficher_score(val, x, y):
    scoreStr = str(val)
    nbZeros  = 6 - len(scoreStr)

    # Zéros de tête
    for i in range(0, nbZeros):
        ecran.blit(chiffresBlancs[0], (x, y))
        x = x + 24

    # Chiffres du score
    for i in range(0, len(scoreStr)):
        for j in range(0, 10):
            if int(scoreStr[i]) == j:
                ecran.blit(chiffresBlancs[j], (x, y))
                x = x + 24


# ============================================================
# victoire_niveau - animation visuelle quand un niveau est gagné
# Paramètres : aucun | Retour : aucun
# ============================================================
def victoire_niveau():
    decor()
    ecran.blit(mGauche, (440, 150))

    if dkMonte <= 30:
        # Pauline sauvée : cœur entier
        afficher_pauline(paulineCalme)
        ecran.blit(coeurPlein, (386, 130))
    else:
        # DK emporte Pauline : cœur brisé
        ecran.blit(coeurBrise, (387, 130))

    if victoireJeu == False:
        # DK s'enfuit vers le haut
        if dkMonte % 30 == 0:
            ecran.blit(imgDK1, (240 - decX1, 160-dkMonte))
        else:
            ecran.blit(imgDK2, (240 - decX2, 160-dkMonte))
    else:
        afficher_dk()


# ============================================================
# ecran_fin - affiche l'écran de fin (Game Over ou Victoire)
# Paramètres : imgFin (image) | Retour : aucun
# ============================================================
def ecran_fin(imgFin):
    ecran.blit(imgFin, (0, 30))

    # Curseur de sélection selon l'option choisie
    if choix == "bas":
        ecran.blit(imgCurseur, (270, 640))
    else:
        ecran.blit(imgCurseur, (270, 575))


# ============================================================
# afficher_confettis - anime les confettis lors de la victoire
# Paramètres : aucun | Retour : aucun
# ============================================================
def afficher_confettis():
    for i in range(0, 400):
        pygame.draw.circle(ecran, confCoul[i], (confX[i], confY[i]), confRayon[i], 0)


# ============================================================
# dessiner_ecran - redessine toute la fenêtre à chaque frame
# Paramètres : aucun | Retour : aucun
# ============================================================
def dessiner_ecran():
    global monteFini, jeuLance, partieFinie, sceneVicFinie, debutFait, afficheDebut

    ecran.fill(NOIR)    # Fond noir

    # --- Écran Game Over ---
    if partieFinie:
        ecran_fin(imgGameOver)
        afficher_score(score, 388, 387)
        afficher_score(meilleurScore, 485, 445)

    # --- Victoire finale ---
    elif victoireJeu:
        if sceneVicAff:
            # Scène de défaite de DK
            victoire_niveau()
            afficher_vies()
            afficher_niveau()
            afficher_score(score, 88, 40)
            afficher_score(meilleurScore, 327, 40)

        elif sceneVicFinie:
            # Écran de victoire avec confettis
            ecran_fin(imgVictoire)
            afficher_confettis()
            afficher_score(score, 388, 387)
            afficher_score(meilleurScore, 485, 445)

    # --- Jeu en cours ---
    else:
        if appuye == False:
            # Écran titre
            ecran.blit(imgTitre, (54, 18))

        elif appuye and introFinie == False:
            # Animation d'introduction
            scene_intro()
            afficher_vies()

        elif introFinie == True and jeuLance == False:
            # Écran de démarrage du niveau
            ecran_debut()
            afficher_vies()
            afficheDebut = True
            debutFait    = True

        elif (jeuLance and victoireNiveau == False) or sceneMort:
            # Jeu en cours ou scène de mort
            decor()
            afficher_dk()
            afficher_mario()
            afficher_pauline(paulineAide)
            afficher_vies()
            if scoreMax == False and sceneMort == False:
                afficher_tonneaux()

        elif victoireNiveau:
            # Séquence de victoire du niveau
            victoire_niveau()
            afficher_vies()

        afficher_niveau()
        afficher_score(score, 88, 40)
        afficher_score(meilleurScore, 327, 40)

    pygame.display.update()


# ============================================================
# PROGRAMME PRINCIPAL
# ============================================================

# Affichage des instructions dans la console
afficher_instructions()

# Initialisation des variables d'état clavier (évite NameError)
monter      = False
descendre   = False
bougerCotes = True
peutGauche  = True
peutDroite  = True

# --- Boucle principale : tourne tant que le joueur veut rejouer ---
while rejouer:

    pygame.init()
    pygame.mixer.init()

    LARGEUR = 800
    HAUTEUR = 800
    ecran   = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption('Donkey Kong – Projet NSI 2025/2026')

    # --- Musique de fond en boucle ---
    try:
        pygame.mixer.music.load(os.path.join("assets", "music.wav"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)   # -1 = boucle infinie
    except Exception:
        pass   # Si le fichier est absent, le jeu continue sans musique

    enPartie = True
    print("Appuie sur ÉCHAP pour quitter.")
    print()

    # --- Boucle de jeu (une partie complète) ---
    while enPartie:

        # === Animation de montée de DK (intro) ===
        if appuye == True and monteFini == False:
            if dkMonte == 0:
                numNiveau = numNiveau + 1       # Nouveau niveau

            if dkMonte == 390:
                pygame.time.delay(500)          # Pause à mi-montée

            if dkMonte >= 560:
                vitMonte = -20                  # DK accélère pour sauter

            if dkMonte != 510 or vitMonte != -20:
                dkMonte = dkMonte + vitMonte
            else:
                monteFini = True                # Fin de la montée

        # === Animation du saut de DK (fin d'intro) ===
        elif monteFini and introFinie == False:
            if numPlat <= 6:
                if dkSautY == 152:
                    dkSautDir = 10              # DK redescend

                if dkSautY == 172:
                    dkSautDir = -10             # DK remonte
                    numPlat   = numPlat + 1     # Une plateforme tombe

                dkSautX = dkSautX - 12          # DK avance vers la gauche

                if numPlat != 6:
                    dkSautY = dkSautY + dkSautDir
                else:
                    introFinie = True
                    pygame.time.delay(1000)

        # === Logique principale du jeu ===
        if jeuLance:

            # Détection de collision Mario/tonneau
            if scoreMax == False and victoireNiveau == False:
                touche = collision()

            # Limites gauche/droite
            peutGauche, peutDroite = limites(mX, mY)

            # --- Mario est en vie ---
            if touche == False:

                monter, descendre, bougerCotes = verif_echelle()

                # Mario atteint le sommet → niveau remporté
                if mY <= 154:
                    victoireNiveau = True
                    dkMonte        = -15
                    vitMonte       = 15
                    mX             = 150
                    mY             = 720
                    imgMario       = mDroite

                # === Gestion du saut ===
                if sautGauche or sautDroite or sautPlace:

                    cptSaut = cptSaut + 1
                    mY      = mY + forceSaut

                    if cptSaut == 7:
                        forceSaut = 7           # Mario redescend

                    if cptSaut == 14:
                        # Saut terminé
                        if ptSaut == 1:
                            score = score + 100 # Bonus : tonneau sauté

                        if sens == "droite":
                            imgMario = mDroite
                            mY       = mY - mvt * cptPente
                        else:
                            imgMario = mGauche
                            mY       = mY + mvt * cptPente

                        # Réinitialisation saut
                        forceSaut  = -7
                        cptSaut    = 0
                        ptSaut     = 0
                        cptPente   = 0
                        sautGauche = False
                        sautDroite = False
                        sautPlace  = False

                    # Déplacement horizontal pendant le saut
                    if mX != 60 and mX != 710 and (mX != 320 or mY >= 232):
                        mvt = pente(mY, mX, sens, "mario")

                        if sautGauche and peutGauche:
                            mX = mX - 5
                        elif sautDroite and peutDroite:
                            mX = mX + 5

                    # Vérifie si Mario saute par-dessus un tonneau
                    for i in range(0, len(tonX)):
                        if mX >= tonX[i] and mX <= tonX[i]+28 and mY <= tonY[i]-23 and mY >= tonY[i]-65:
                            ptSaut = 1

                # === Déplacement et logique des tonneaux ===
                if scoreMax == False:

                    for i in range(0, len(imgTon)):

                        # Tonneau sorti du niveau → disparaît
                        if tonX[i] <= 31:
                            tonX[i] = -30
                            tonY[i] = -30

                        # Vérifie si le tonneau doit tomber par le bord
                        if chute[i] == False:
                            tonGauche[i], tonDroite[i] = limites(tonX[i], tonY[i]-15)
                            if tonGauche[i] == False or tonDroite[i] == False:
                                chute[i] = True

                        # Direction du tonneau selon sa position verticale
                        if (tonY[i] <= 255 and tonY[i] >= 243) or \
                           (tonY[i] <= 452 and tonY[i] >= 415) or \
                           (tonY[i] <= 648 and tonY[i] >= 611):
                            tonSens[i] = "droite"

                        elif (tonY[i] <= 353 and tonY[i] >= 317) or \
                             (tonY[i] <= 550 and tonY[i] >= 513) or \
                             (tonY[i] <= 731 and tonY[i] >= 709):
                            tonSens[i] = "gauche"

                        # Le tonneau roule sur la plateforme
                        if chute[i] == False:
                            if tonSens[i] == "droite":
                                tonX[i] = tonX[i] + 10
                            else:
                                tonX[i] = tonX[i] - 10

                            tonY[i] = pente(tonY[i]-11, tonX[i], tonSens[i], "tonneau")
                            tonY[i] = tonY[i] + 11

                        else:
                            # Tonneau en train de tomber par le bord
                            cptChute[i] = cptChute[i] + 1

                            if tonGauche[i] == False:
                                tonX[i] = tonX[i] - 5
                            elif tonDroite[i] == False:
                                tonX[i] = tonX[i] + 5

                            tonY[i] = tonY[i] + 7

                            if cptChute[i] == 8:
                                # Atterrissage sur la plateforme suivante
                                tonY[i]     = tonY[i] + 6
                                cptChute[i]  = 0
                                chute[i]     = False
                                tonGauche[i] = True
                                tonDroite[i] = True

                        # Animation de rotation du tonneau
                        if imgTon[i] == seqTon[3]:
                            imgTon[i] = seqTon[0]
                        else:
                            for j in range(0, len(seqTon)-1):
                                if imgTon[i] == seqTon[j]:
                                    imgTon[i] = seqTon[j+1]

                    # DK décide aléatoirement de lancer un tonneau
                    if lanceTonneau == False:
                        choixDK = random.randint(0, 50 - diff)
                        if choixDK == 0:
                            imgDK        = dkGauche
                            lanceTonneau = True
                        else:
                            imgDK        = dkFace
                            lanceTonneau = False

                    if lanceTonneau:
                        cptLance = cptLance + 1

                        if cptLance == 20:
                            # DK lance le tonneau
                            imgDK = dkDroite
                            tonX.append(250)
                            tonY.append(243)
                            tonSens.append("droite")
                            imgTon.append(ton1)
                            chute.append(False)
                            cptChute.append(0)
                            tonGauche.append(True)
                            tonDroite.append(True)

                        if cptLance == 40:
                            # Fin du lancer
                            cptLance     = 0
                            imgDK        = dkFace
                            lanceTonneau = False

            # --- Mario touché : séquence de mort ---
            else:
                if sceneMort == False:
                    if cptMort == 0:
                        mY = mY + 10        # Ajuste la position du mort

                    cptMort  = cptMort + 1
                    imgMario = mMort

                    if cptMort == 60:
                        # Fin de la scène de mort : perte d'une vie
                        sceneMort = True
                        cptMort   = 0
                        vies      = vies - 1

                else:
                    # Réinitialisation du niveau après la mort
                    debutFait    = False
                    jeuLance     = False
                    lanceTonneau = False
                    sceneMort    = False
                    touche       = False
                    sautGauche   = False
                    sautDroite   = False
                    sautPlace    = False
                    tonX         = []
                    tonY         = []
                    imgTon       = []
                    cptLance     = 0
                    tonSens      = []
                    chute        = []
                    cptChute     = []
                    tonGauche    = []
                    tonDroite    = []
                    cptPente     = 0
                    ptSaut       = 0
                    mX           = 150
                    mY           = 720
                    forceSaut    = -7
                    cptSaut      = 0
                    sens         = "droite"
                    imgMario     = mDroite

                # Plus de vies → Game Over
                if vies < 0:
                    partieFinie = True
                    if score > meilleurScore:
                        meilleurScore = score

        # === Score maximum → victoire automatique ===
        if score >= 999999:
            score    = 999999               # Score maximum affichable
            scoreMax = True
            imgDK    = dkDefaite

        # === Gestion de la victoire de niveau ===
        if victoireNiveau:
            if numNiveau == 5 or scoreMax:
                # Fin de partie (5 niveaux ou score max atteint)
                if sceneVicFinie == False:
                    imgDK       = dkDefaite
                    sceneVicAff = True
                else:
                    # Animation des confettis
                    for i in range(0, 400):
                        confY[i] = confY[i] + confVit[i]

                    if score > meilleurScore:
                        meilleurScore = score

                jeuLance    = False
                victoireJeu = True

            else:
                # Passage au niveau suivant
                dkMonte = dkMonte + vitMonte

                if dkMonte == 15:
                    score = score + 250     # Bonus sauvegarde Pauline
                    pygame.time.delay(1000)

                # Animation DK : sans Pauline d'abord
                if dkMonte <= 30:
                    imgDK1 = dkVide1;  imgDK2 = dkVide2
                    decX1  = 0;        decX2  = 0
                else:
                    # Puis DK tient Pauline
                    imgDK1 = dkMonte1; imgDK2 = dkMonte2
                    decX1  = 13;       decX2  = 35

                if dkMonte == 150:
                    # Réinitialisation pour le niveau suivant
                    victoireNiveau = False
                    monteFini      = False
                    introFinie     = False
                    debutFait      = False
                    jeuLance       = False
                    lanceTonneau   = False
                    sautGauche     = False
                    sautDroite     = False
                    sautPlace      = False
                    touche         = False
                    tonX           = []
                    tonY           = []
                    imgTon         = []
                    tonSens        = []
                    chute          = []
                    cptChute       = []
                    tonGauche      = []
                    tonDroite      = []
                    cptPente       = 0
                    dkMonte        = 0
                    numPlat        = 0
                    vitMonte       = 15
                    dkSautX        = 378
                    dkSautY        = 172
                    dkSautDir      = 0
                    forceSaut      = -7
                    cptSaut        = 0
                    sens           = "droite"

                    diff = diff + 8         # Jeu plus difficile au prochain niveau

        # === Gestion des événements clavier ===
        pygame.event.get()
        touches = pygame.key.get_pressed()

        # ÉCHAP → quitter
        if touches[pygame.K_ESCAPE]:
            if score > meilleurScore:
                meilleurScore = score
            enPartie = False
            rejouer  = False

        # ESPACE → démarrer l'intro
        if touches[pygame.K_SPACE]:
            appuye = True

        # Active les commandes si le jeu est en cours ou sur un menu
        if (jeuLance and sautGauche == False and sautDroite == False and sautPlace == False and victoireNiveau == False and touche == False) or partieFinie or victoireJeu:

            # Flèche GAUCHE → déplacer Mario à gauche
            if touches[pygame.K_LEFT] and bougerCotes and (mX != 320 or mY > 232) and peutGauche and mX != 60:
                mY = pente(mY, mX, sens, "mario")

                if sens == "gauche":
                    mX = mX - 5

                if imgMario == mGauche:
                    imgMario = mCourseG
                else:
                    imgMario = mGauche

                if touches[pygame.K_SPACE]:
                    sautGauche = True
                    imgMario   = mSautG

                sens = "gauche"

            # Flèche DROITE → déplacer Mario à droite
            elif touches[pygame.K_RIGHT] and bougerCotes and peutDroite and mX != 710:
                mY = pente(mY, mX, sens, "mario")

                if sens == "droite":
                    mX = mX + 5

                if imgMario == mDroite:
                    imgMario = mCourseD
                else:
                    imgMario = mDroite

                if touches[pygame.K_SPACE]:
                    sautDroite = True
                    imgMario   = mSautD

                sens = "droite"

            # Flèche HAUT → monter une échelle / menu vers le haut
            elif touches[pygame.K_UP] and (monter or partieFinie or victoireJeu):
                if monter:
                    mY = mY - 5
                    if imgMario == mEchelle1:
                        imgMario = mEchelle2
                    else:
                        imgMario = mEchelle1

                if partieFinie or victoireJeu:
                    choix = "haut"

            # Flèche BAS → descendre une échelle / menu vers le bas
            elif touches[pygame.K_DOWN] and (descendre or partieFinie or victoireJeu):
                if descendre:
                    mY = mY + 5
                    if imgMario == mEchelle1:
                        imgMario = mEchelle2
                    else:
                        imgMario = mEchelle1

                if partieFinie or victoireJeu:
                    choix = "bas"

            # ESPACE → saut sur place
            if touches[pygame.K_SPACE] and sautGauche == False and sautDroite == False and bougerCotes:
                sautPlace = True
                if sens == "droite":
                    imgMario = mSautD
                else:
                    imgMario = mSautG

            # ENTRÉE → valider dans le menu de fin
            if touches[pygame.K_RETURN] and (partieFinie or victoireJeu):

                # Option HAUT : Rejouer → réinitialisation complète
                if choix == "haut":
                    enPartie       = False
                    victoireNiveau = False
                    appuye         = False
                    monteFini      = False
                    introFinie     = False
                    jeuLance       = False
                    debutFait      = False
                    partieFinie    = False
                    lanceTonneau   = False
                    sautGauche     = False
                    sautDroite     = False
                    sautPlace      = False
                    victoireJeu    = False
                    sceneMort      = False
                    scoreMax       = False
                    sceneVicFinie  = False
                    sceneVicAff    = False
                    touche         = False
                    score          = 0
                    numNiveau      = 0
                    dkMonte        = 0
                    vitMonte       = 15
                    numPlat        = 0
                    dkSautX        = 378
                    dkSautY        = 172
                    dkSautDir      = 0
                    mX             = 150
                    mY             = 720
                    forceSaut      = -7
                    cptSaut        = 0
                    ptSaut         = 0
                    cptMort        = 0
                    cptPente       = 0
                    vies           = 2
                    diff           = 0
                    sens           = "droite"
                    imgMario       = mDroite
                    choix          = "haut"
                    tonX           = []
                    tonY           = []
                    imgTon         = []
                    cptLance       = 0
                    tonSens        = []
                    chute          = []
                    cptChute       = []
                    tonGauche      = []
                    tonDroite      = []

                # Option BAS : Quitter
                elif choix == "bas":
                    enPartie = False
                    rejouer  = False

        # Redessine l'écran si la partie est active
        if enPartie:
            dessiner_ecran()
            pygame.time.delay(30)           # ~30 fps

        # Garde l'écran de démarrage affiché plus longtemps
        if afficheDebut:
            pygame.time.delay(2000)
            afficheDebut = False
            jeuLance     = True

        # Garde la scène de victoire affichée plus longtemps
        if sceneVicAff:
            pygame.time.delay(2500)
            sceneVicAff   = False
            sceneVicFinie = True

    pygame.quit()

# ============================================================
# Fin du programme
# ============================================================
