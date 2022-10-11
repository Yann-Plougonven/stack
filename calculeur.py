from stack import Stack  # Ne pas mettre le .py à la fin
expressions = [('3', '4', '*', '2', '+'), ('2', '4', '+', '6', '-', '1', '+'), ('1', '19', '+', '2', '-'), ('0', '2', '-', '2', '+', '10', '-'), ('2', '3', '4', '+', '*')]
operateurs = ('+', '-', '*')
resultats = []


def resultat(expression):
    """Retourne le résultat de l'expression
    NSI si l'expression donnée en entrée est bonne"""
    p = Stack()  # p est instance de Stack
    nbs_pour_op = []
    result = 0  # On initialise le résultat de l'opération en cours de traitement à 0.
    for char in expression:  # Pour chaque caractère de l'expression
        if char in operateurs:  # Si '+', '-', '*'
            op1 = float(p.pop())
            op2 = float(p.pop())

            if char == "+":
                result = op1 + op2

            elif char == "-":
                result = op2 - op1

            elif char == "*":
                result = op1 * op2

            p.push(result)

        else:  # Si chiffre
            p.push(char)  # Ajouter le chiffre à la liste p
            
    return p.summit()  # Retourne une fois tous les caractères traités


for e in expressions:
    resultats.append(resultat(e))
print(resultats)