import itertools

def solve_cryptarithmetic():
    # Unique letters in the puzzle
    letters = 'SENDMORY'
    assert len(letters) <= 10, "Too many unique letters in the puzzle!"

    # Generate all permutations of digits 0-9 of length equal to the number of unique letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Map the letters to digits
        mapping = dict(zip(letters, perm))
        
        # Ensure that leading letters don't map to zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        
        # Convert words to their corresponding integer values based on current mapping
        send = 1000 * mapping['S'] + 100 * mapping['E'] + 10 * mapping['N'] + mapping['D']
        more = 1000 * mapping['M'] + 100 * mapping['O'] + 10 * mapping['R'] + mapping['E']
        money = 10000 * mapping['M'] + 1000 * mapping['O'] + 100 * mapping['N'] + 10 * mapping['E'] + mapping['Y']
        
        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print("Mapping:", mapping)
            return True

    print("No solution found.")
    return False

# Example usage
solve_cryptarithmetic()
