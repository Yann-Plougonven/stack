from stack import Stack  # Ne pas mettre le .py à la fin

expressions = [('3', '4', '*', '2', '+')]
operateurs = ('+', '-', '*')
resultats = []


def resultat(expression):
    """Cette fonction ne retourne le bon résultat que si l'expression donnée en entrée est bonne"""
    p = Stack()  # p est instance de Stack
    liste = []
    for char in expression:  # Pour chaque caractère
        if char in operateurs:
            cond = True
            while cond == True:
                try:
                    liste.append(p.pop())
                    print(f"liste = {liste}")
                except IndexError:
                    if char == "+":
                        result = int(liste[0]) + int(liste[1])
                        p.push(result)
                        cond = False
                        liste = []
                    if char == "-":
                        result = int(liste[0]) - int(liste[1])
                        p.push(result)
                        cond = False
                        liste = []
                    if char == "*":
                        result = int(liste[0]) * int(liste[1])
                        p.push(result)
                        cond = False
                        liste = []

        else:  # Si chiffre
            p.push(char)
    return p.summit()


for e in expressions:
    resultats.append(resultat(e))
print(resultats)
