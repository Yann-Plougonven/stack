from stack import Stack  # Ne pas mettre le .py à la fin


expressions = ['2x(x+1)','2x((x+1)','2x+1)', '2x(x+1)(x+2)(x+3)','2x(x+1)(x+2)((x+3)','2x(x+1)(x+2))(x+3)','','(','()',')(']
resultats_expressions = []


def parse_checker(string):
    p = Stack()
    p2 = Stack()
    for letter in string:
        if letter == "(":
            p.push("(")
        
        elif letter == ")":
            try:
                p.pop()
            except IndexError:
                return False
            
        if letter == "[":
            p2.push("[")
            
        elif letter == "]":
            p2.pop
            try:
                p2.pop()
            except IndexError:
                return False
        
        
    if p.isEmpty() == True and p2.isEmpty() == True:
        return True
    else:
        return False
    
    
    
for e in expressions:
    resultats_expressions.append(parse_checker(e))

print(resultats_expressions)