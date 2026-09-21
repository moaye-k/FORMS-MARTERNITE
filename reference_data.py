# -*- coding: utf-8 -*-
"""Données de référence pour l'enquête E-CNPS Maternité."""

INITIATEURS = [
    "Moi-même",
    "Moi-même avec l'aide de l'employeur",
    "Mon employeur / service RH",
    "Un proche m'a aidée",
]
# Si l'utilisatrice choisit cette valeur, elle n'a pas utilisé l'outil elle-même
# -> on saute toute la PARTIE 1 (Q2 a Q10) et on va direct en PARTIE 2 (Q11).
INITIATEUR_SANS_OUTIL = "Mon employeur / service RH"

PREMIERE_DEMANDE = ["Oui, première demande", "Non, déjà fait en agence", "Non, déjà fait en ligne"]

MOMENT_DEMANDE = ["Avant l'accouchement (prénatal)", "Après l'accouchement", "En plusieurs temps"]

SUPPORT = ["Téléphone mobile", "Ordinateur", "Les deux"]

SATISFACTION_ROWS = [
    ("p1_acces", "Accès / connexion au compte sur E-CNPS"),
    ("p1_comprehension_pieces", "Compréhension des pièces à fournir (certificats, bulletins, acte de naissance…)"),
    ("p1_televersement", "Téléversement / envoi des documents en ligne"),
    ("p1_suivi", "Suivi de l'état d'avancement du dossier"),
    ("p1_info_montant", "Information sur le calcul et le montant de l'indemnité"),
    ("p1_delai_versement", "Délai jusqu'au versement de l'indemnité"),
]
SATISFACTION_SCALE = ["Très satisfait(e)", "Satisfait(e)", "Insatisfait(e)", "Très insatisfait(e)"]

CES = ["Très facile", "Facile", "Difficile", "Très difficile"]

ERGONOMIE_ROWS = [
    ("erg_clarte_ecrans", "Clarté et simplicité des écrans"),
    ("erg_trouver_rubrique", "Facilité à trouver la rubrique « indemnités de maternité »"),
    ("erg_liste_pieces", "Clarté de la liste des pièces à fournir"),
    ("erg_televerser", "Facilité pour téléverser / photographier les documents"),
    ("erg_vocabulaire", "Clarté du vocabulaire employé"),
    ("erg_messages", "Qualité des messages de confirmation et des aides"),
    ("erg_mobile", "Confort d'utilisation sur téléphone"),
    ("erg_accessibilite", "Accessibilité en période de fatigue (fin de grossesse / post-partum)"),
]
ERGONOMIE_SCALE = ["Excellent", "Bon", "Passable", "Mauvais"]

AIDE = [
    "Non, j'ai tout fait seule",
    "Oui, aide de l'employeur / RH",
    "Oui, appui du centre de relation client",
    "Oui, déplacement en agence malgré tout",
]

CSAT = ["Très satisfait(e)", "Satisfait(e)", "Insatisfait(e)", "Très insatisfait(e)"]

DELAI = ["Plus rapide que prévu", "Conforme à mes attentes", "Plus lent que prévu", "Sans comparaison"]

CONFIANCE = ["Tout à fait", "Plutôt", "Plutôt pas", "Pas du tout"]
