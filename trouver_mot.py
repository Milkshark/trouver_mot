#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-
from itertools import permutations 
import csv

tsv_file = open("Lexique383.tsv",encoding="utf_8")
dictionnaire = csv.reader(tsv_file, delimiter="\t")
dico= []

for row in dictionnaire:
    ligne = []
    for i in range(35):
        ligne.append(str(row[i]))
        
    dico.append(ligne)
tsv_file.close()


def trouve_mot(WSEARCH,TYPE):
    'Renvoie une liste de mots ressemblant'
    #AUX, ADJ, ADV, ART, CON, LIA, NOM, ONO, PRE, PRO, VER
    similaire = []

    for WORD in dico:
        if len(WSEARCH) == len(WORD[0]) and ((TYPE in WORD[28]) or TYPE == 'ALL'):
            SIM = 1
            for i in range(len(WORD[0])):
                if WSEARCH[i] == "*":
                    SIM*=1
                else:
                    if WSEARCH[i] != WORD[0][i]:
                        SIM*=0
            if SIM ==1:
                similaire.append(WORD[0])
    return(similaire)

##>>> trouve_mot("b**j**r",'ALL')
##['bonjour']
