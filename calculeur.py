from stack import Stack  # Ne pas mettre le .py à la fin

# ATTENTION : Y'a des petits problèmes pour les oppérations avec des '-' (par exemple si on remplacer '0' par '10' ci-dessous)
expressions = [('3', '4', '*', '2', '+'), ('2', '4', '+', '6', '-', '1', '+'), ('1', '19', '+', '2', '-'), ('0', '2', '-', '2', '+', '10', '-')]
operateurs = ('+', '-', '*')
resultats = []


def resultat(expression):
    """Cette fonction ne retourne le bon résultat que si l'expression donnée en entrée est bonne"""
    p = Stack()  # p est instance de Stack
    nbs_pour_op = []
    result = 0  # On initialise le résultat de l'opération en cours de traitement à 0.
    for char in expression:  # Pour chaque caractère de l'expression
        if char in operateurs:  # Si '+', '-', '*'
            cond = True
            while cond == True:
                try:
                    nbs_pour_op.append(p.pop())  # On ajoute tous les nombres de p à la liste "nbs_pour_op"
                except IndexError:  # Si p est vide, on lance les calculs
                    i = -1

                    if char == "+":
                        result = 0  # On initialise le résultat de l'opération en cours de traitement à 0.
                        for a in nbs_pour_op:
                            i += 1
                            result = result + int(nbs_pour_op[i])

                    elif char == "-":
                        for a in nbs_pour_op[-2]:  # Nombre de terme dans nb_pour_op -1
                            i += 1
                            result = result - int(nbs_pour_op[i])

                    elif char == "*":
                        result = 1 # On initialise le résultat de l'opération en cours de traitement à 1.
                        for a in nbs_pour_op:
                            i += 1
                            result = result * int(nbs_pour_op[i])

                    p.push(result)
                    cond = False  # On arrête la bouche while
                    nbs_pour_op = []
        else:  # Si chiffre
            p.push(char)
    return p.summit()  # Retourne une fois tous les caractères traités


for e in expressions:
    resultats.append(resultat(e))
print(resultats)