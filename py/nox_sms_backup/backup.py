#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import os
import json

from datetime import datetime
from hashlib import md5

DEFAULT_REP = "messages"
DEFAULT_BACKUP = "messages/sms_backup.json"

class SMS:
    """
        Représentation d'un SMS avec :
            1 expéditeur ou un destinataire selon qu'il a été envoyé ou reçu
            1 date
            1 texte
    """

    regexp = re.compile(r"(?P<texte>.+),'(?P<nom>[^,]*),(?P<date>[^,]*),$")

    def __init__(self, date=0, texte="", expediteur="", destinataire="", parse=None, not_sent=None):
        """
            Le constructeur permet de remplir les champs séparément ou de parser une source.
            Il crée ensuite une somme md5 du message pour fournir un identifiant unique.
        """
        if parse is not None:
            valide = self.parse(parse, not_sent)
        else:
            valide = True
            self.expediteur = expediteur
            self.destinataire = destinataire
            self.date = date
            self.texte = texte

        if valide:
            self.id = md5("{}-{}-{}".format(self.expediteur or self.destinataire, self.date, self.texte))
            self.id = self.id.hexdigest()
        else:
            self.id = None

    def __repr__(self):
        return "<SMS {}{} le {}>".format(self.expediteur or "@", self.destinataire or "@", self.date)

    def __str__(self):
        return self.texte

    def __unicode__(self):
        return self.texte

    def parse(self, texte, not_sent):
        """
            Récupère une ligne de texte, rempli les champs correspondants et renvoie False  
            Si la correspondance ne peut être rétablie, renvoie False

            not_sent permet de spécifier si le nom est bien celui de l'expéditeur
        """
        resultat = self.regexp.search(texte)
        if resultat is not None:
            infos = resultat.groupdict()
            if not_sent:
                self.expediteur, self.destinataire = infos["nom"], ""
            else:
                self.expediteur, self.destinataire = "", infos["nom"]

            self.texte = infos["texte"]

            self.date = datetime.strptime(infos["date"], "%d/%m/%Y %H:%M:%S")

            return True

        else:
            print("Echec pour : \n<<<\n    {}>>>".format(texte))
            return False

def main():
    if False: #FIXME : parse args
        rep = "some rep"
    else:
        rep = DEFAULT_REP

    chaine="Liste des fichiers :"
    print(chaine + "\n" + "="*len(chaine))

    # contient des tuples avec un booléen pour savoir
    # si c'est envoyé (faux) ou reçu (vrai) et le nom du fichier
    fichiers = {}
    regexp = re.compile(r"^ExportedMessages\.[^.]*\.?(csv|txt)$")
    for filename in os.listdir(DEFAULT_REP):
        if regexp.match(filename):
            not_sent = "ent" not in filename
            fichiers[filename] = not_sent
            print("\t* {}".format(filename))

    # on parcours les lignes de chaque fichier
    lignes = []
    ligne_en_cours = ""
    for fichier, not_sent in fichiers.items():
        with open("{}/{}".format(DEFAULT_REP, fichier)) as file: #FIXME : codecs
            for line in file:
                ligne_en_cours += line.replace("\x00", "") + "\n" #ajoute le texte nettoyé

                if ",\x00'" in line:
                    lignes.append(ligne_en_cours[:-1]) # sans le \n restant
                    ligne_en_cours=""
        fichiers[fichier] = (not_sent, lignes)


    if os.path.exists(DEFAULT_BACKUP):
        with open(DEFAULT_BACKUP) as file:
            all_sms = json.load(DEFAULT_BACKUP)
    else:
        all_sms = {}
    
    for fichier, infos in fichiers.items():
        for sms_brut in infos[1]:
            sms=SMS(parse=sms_brut, not_sent=infos[0])

            if sms.id is not None and sms.id not in all_sms.keys():
                all_sms[sms.id] = sms

    with open(DEFAULT_BACKUP, "wb") as file:
        json.dump(all_sms, file)

if __name__ == '__main__':
    main()