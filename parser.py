from stack import Stack  # Ne pas mettre le .py à la fin
expressions = ['2x(x+1)','2x((x+1)','2x+1)', '2x(x+1)(x+2)(x+3)','2x(x+1)(x+2)((x+3)','2x(x+1)(x+2))(x+3)','','(','()',')(']
resultats_expressions = []

def parse_checker(string):
    p = Stack()
    for letter in string:
        if letter == "(":  # Ajouter les "(" à resultats_expressions
            p.push("(")
        if letter == "[":  # Ajouter les "[" à resultats_expressions
            p.push("[")
        
        
        elif letter == ")":  # Si ")"
            try:  
                if p.summit() == "(":  # Si le dernier caractère de la file est "("
                    p.pop()   
                else:
                    return False 
            except IndexError:
                return False

            
        elif letter == "]":  # Si "]"
            try:
                if p.summit() == "[":        
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