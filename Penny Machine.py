def penny_puzzle_brute_force(machine):
    # Get length of the machine (number of boxes)
    N = len(machine)
    # Initialize iteration count
    iteration_count = 0
    
    # Apply the Brute Force algorithm on the machine
    while any(p >= 2 for p in machine):
        # Iterate through every box in the machine
        for i in range(N - 1):
            # Check if current box has 2 or more pennies
            if machine[i] >= 2:
                # Deduct 2 pennies from current box
                machine[i] -= 2
                # Add 1 penny to box directly to the right
                machine[i + 1] += 1
                # Increment iteration counter
                iteration_count += 1
    
    return machine, iteration_count

# Function call
x = [6, 0, 0, 0, 0]

Fx, iteration_count_x = penny_puzzle_brute_force(x)

print("Iteration count for x:", iteration_count_x)
print("Final state for x:", Fx)
