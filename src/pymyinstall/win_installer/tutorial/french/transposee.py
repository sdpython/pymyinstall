#-*- coding: utf-8 -*-
# il faut toujours ceci au début du programme pour
# pouvoir mettre des accents dans le programme

# python ne fait pas grand chose mais il a plein de librairie
# en voici deux
import pandas
import os

###################
# retourner la matrice
###################

# changer False en True pour exécuter le code qui suit
if False:
    # on charge une feuille dans ce qu'on appelle un dataframe (chercher sur
    # wikipedia)
    df = pandas.read_excel("calories_a.xlsx")

    # on prend la transposée (les colonnes deviennent des lignes et
    # réciproquement)
    t = df.T

    # on stocke le résultat dans un autre fichier
    t.to_excel("calories_transposee.xlsx")

###################
# prendre plein de fichiers excel pour n'en faire qu'une seule table
###################

# changer False en True pour exécuter le code qui suit
if True:
    # données extraites depuis http://www.les-calories.com/calories-a.html

    # on récupère le contenu du répertoire
    fichiers = os.listdir(".")

    # on ne garde que les fichiers excel
    excel = [fichier for fichier in fichiers if "xlsx" in fichier]

    # on fait un print pour vérifier qu'on ne s'est pas trompé
    # normalement, tout s'affiche bien
    print(excel)

    # on ne garde que les fichiers qui ne contiennent pas transposee ni tout
    excel = [
        fichier for fichier in excel if "transposee" not in fichier and "tout" not in fichier]
    print(excel)

    # on charge tout les fichiers dans des dataframe
    liste = []
    for fichier in excel:
        print("lecture de ", fichier)
        df = pandas.read_excel(fichier)
        print("dimension", df.shape)
        liste.append(df)

    # on concatène le tout
    tout = pandas.concat(liste)
    print("dimension du tout", tout.shape)

    # on sauve le tout dans un unique fichier
    tout.to_excel("tout.xlsx")
