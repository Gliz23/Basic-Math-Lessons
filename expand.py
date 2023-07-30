#This function works for x(n-1) questions. Where x is a digit between 0-9.
def expand_expression(expression):
    terms = expression.split('*')

    storage =[]
    expand_form=[]
    small_storage=[]

    for term in terms:
        if '(' in term and ')' in term:
            term = term.replace('(','').replace(')','')
        storage.append(term)

    for item in storage:
        bracket_items = item.split('-')
        small_storage.append(bracket_items)
                       
            

    # for thing in small_storage:
    #     print(thing)

    answer = f"{small_storage[0]} * {small_storage[1]} * {small_storage[2][0]} + {small_storage[0]} * {small_storage[1]} * {small_storage[2][1]}"
    answer = answer.replace('[','').replace(']','').replace("'","").replace("'","").replace('1','')/replace('*','').replace(' ','').replace('nn','n^2')
    print(answer)
    return answer

    

#Your arguments should be seperated by '*' where there is multiplication.
example = expand_expression("7*n*(n-1)")





