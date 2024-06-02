def toggle_switches(start, end):
    # Base case for 1 switch,only 1 move required 
    if start == end: 
        switches[start] = 1 - switches[start]  # toggle 1 to 0
        return 1
    # Base case for 2 switches,requires 2 moves
    if end - start == 1:
        switches[start] = 1 - switches[start]  
        switches[end] = 1 - switches[end]     
        return 2

    total_moves = 0

    # To turn off current switch, all switches to the right except the one at immediate right need to be off 
    # so we toggle off all switches from start +2 (to skip the first and second one)
    turn_off_without_first_2_num_moves = toggle_switches(start + 2, end)
    total_moves += turn_off_without_first_2_num_moves
    
    # Now that all are on except last one, we can toggle the first one to be off
    switches[start] = 0
    total_moves += 1

    # We now need to turn 'start + 2' switches back on to be able to turn off the second one
    turn_on_without_first_2_num_moves = toggle_switches(start + 2, end)
    total_moves += turn_on_without_first_2_num_moves

    # First switch is off and complete, we can ignore it & turn off start +1 by calling function toggle_switches 
    total_moves += toggle_switches(start + 1, end)
    
    return total_moves
n = 3
switches = [1] * n  # Initialize all switches to 1 ('on')

print("Initial Switches:", switches)

min_moves = toggle_switches(0, len(switches) - 1) 
print("Min Moves Required:", min_moves)
print("Switches After Toggling:", switches)

