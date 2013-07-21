#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import os
import json

from codecs import open
from datetime import datetime
from hashlib import md5

DEFAULT_REP = "messages"
DEFAULT_BACKUP = "messages/sms_backup.json"

all_sms = ""

class SMS:
    """
        Représentation d'un SMS avec :
            1 expéditeur ou un destinataire selon qu'il a été envoyé ou reçu
            1 date
            1 texte
    """

    regexp = re.compile(r"(?P<texte>.+),'(?P<nom>[^,]*),(?P<date>[^,]*),$")

    def __init__(self, date=0, texte="", expediteur=None, destinataire=None, parse=None, not_sent=None):
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

    def jsonable(self):
        return {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d_%H:%M:%S"),
            "texte": self.texte,
            "expediteur": self.expediteur,
            "destinataire": self.destinataire,
        }

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
        with open("{}/{}".format(DEFAULT_REP, fichier), encoding="utf-16-le") as file: #FIXME : codecs
            for line in file:
                ligne_en_cours += line + "\n" #ajoute le texte nettoyé

                if ",'" in line:
                    lignes.append(ligne_en_cours[:-1]) # sans le \n restant
                    ligne_en_cours=""
        fichiers[fichier] = (not_sent, lignes)

    # on charge la sauvegarde si elle existe
    if os.path.exists(DEFAULT_BACKUP):
        with open(DEFAULT_BACKUP) as file:
            try:
                all_sms = json.load(file)
                json_charge = True
            except ValueError:
                json_charge=False;all_sms = {} #raise Exception("Le fichier JSON n'est pas valide.")
    else:
        all_sms = {}
        json_charge = False
    
    # enregistre les SMS
    for fichier, infos in fichiers.items():
        for sms_brut in infos[1]:
            sms=SMS(parse=sms_brut, not_sent=infos[0])

            if sms.id is not None and sms.id not in all_sms.keys():
                all_sms[sms.id] = sms

    # on sauvegarde et on backup si nécessaire
    if json_charge:
        with open(DEFAULT_BACKUP) as original_file:
            with open(
                    "{}.{}.bak".format(
                        DEFAULT_BACKUP, 
                        datetime.now().strftime("%Y-%m-%d_%Hh%Mmin%Ss")
                    )
                ) as backup_file:
                for line in original_file:
                    backup_file.write(line)

    with open(DEFAULT_BACKUP, "wb") as file:
        for i, sms in enumerate(all_sms.values()):
            printi)
            json.dump(sms.jsonable(), file)

if __name__ == '__main__':
    main()