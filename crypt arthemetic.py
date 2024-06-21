from itertools import permutations

def solve_cryptarithm():

    letters = 'SENDMOREY'
    
    digits = '0123456789'
   
    for perm in permutations(digits, len(letters)):
       
        mapping = dict(zip(letters, perm))
        
        
        if mapping['S'] == '0' or mapping['M'] == '0':
            continue
        
       
        send = int("".join(mapping[letter] for letter in 'SEND'))
        more = int("".join(mapping[letter] for letter in 'MORE'))
        money = int("".join(mapping[letter] for letter in 'MONEY'))
        
        
        if send + more == money:
            return send, more, money, mapping
    
    return None


solution = solve_cryptarithm()

if solution:
    send, more, money, mapping = solution
    print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
    print("Mapping:", mapping)
else:
    print("No solution found")
