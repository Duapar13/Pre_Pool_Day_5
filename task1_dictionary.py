# Create a dictionary stored in a student variable.
# This dictionary must contain 2 key/value pairs.
# The keys must be “name” and “academic_year”.
# The associated values are up to you, but please keep them coherent!

etudiants = []

etudiant1 = {
    "nom": "William Berger",
    "annee": 3
}

etudiant2 = {
    "nom": "Bastien Rapaud",
    "annee": 3
}

etudiant3 = {
    "nom": "Mathieu Pigot",
    "annee": 5
}
etudiants.append(etudiant1)
etudiants.append(etudiant2)
etudiants.append(etudiant3)

for etudiant in etudiants:
    print(etudiant)
