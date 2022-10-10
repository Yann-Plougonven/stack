from stack import Stack  # Ne pas mettre le .py à la fin
expressions = ['2x(x+1)','2x((x+1)','2x+1)', '2x(x+1)(x+2)(x+3)','2x(x+1)(x+2)((x+3)','2x(x+1)(x+2))(x+3)','','(','()',')(']
resultats_expressions = []

codes = {")":"(", "]":"[", "}":"{"}

def parse_checker(string):
    p = Stack()
    for letter in string:
        if letter in codes.values():  # Si (, [, {
            p.push(letter)
        elif letter in codes.keys():  # Si ), ], }
            try:
                if codes[letter] == p.summit():     
                    p.pop()
                else:
                    return False
            except IndexError:
                return False


    if p.isEmpty() == True:
        return True
    else:
        return False

for e in expressions:
    resultats_expressions.append(parse_checker(e))

print(resultats_expressions)