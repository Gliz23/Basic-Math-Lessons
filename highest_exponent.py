def find_highest_term(runtime_func):
       
     # Split the runtime function into its individual terms
    terms = runtime_func.split('+')

     # Remove any leading or trailing whitespace from each term
    terms = [term.strip() for term in terms]

     # Initialize the highest exponent to None
    highest_exponent = None

     # Iterate over each term and update the highest exponent if necessary
    for term in terms:
         # Check if the term is a polynomial of the form an^b
        if 'n' in term and '^' in term:
             # Split the term into its coefficient and exponent
            coeff, exponent = term.split('^')

            if highest_exponent is None or exponent > highest_exponent:
                highest_exponent = exponent
            else:
                continue
    if highest_exponent is None:
        return None

             
    term_str = f"n^{int(highest_exponent)}"
    return term_str

eg = find_highest_term("7n^2+7n")
print(eg)

