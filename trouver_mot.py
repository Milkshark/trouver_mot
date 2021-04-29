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
#tsv_file.close()

def ty():
    TYPES = []
    for word in dico:
        list_type = word[28].split(',')
        for e in list_type:
            if not(e in TYPES):
                TYPES.append(e)
    return(TYPES)

def trouve_mot(WSEARCH,TYPE):
    'sea*ch, ADJ;NOM;VER;ADV;AUX;PRE;ONO:CON'
    #ONOmatopée, ADJectif, ADVerbe, VERbe, AUXiliaire...
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
            
            

def lettre(mot):
    les_lettres = []
    mots_valides = []
    for c in mot:
        les_lettres.append(c)
    perm = permutations(les_lettres) 
    les_perm = []
    for p in perm:
        les_perm.append(p)
    
    for permutation in les_perm:
        mot_permute = ''
        for c in permutation:
            mot_permute += c
        
        if mot_permute in dico:
            mots_valides.append(mot_permute)

    return (mots_valides)

# Print the obtained permutations 

