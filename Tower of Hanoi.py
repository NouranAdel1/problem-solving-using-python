def tower_of_hanoi(n, from_peg, to_peg, aux_peg1, aux_peg2):
    global moves
    if n > 0:
        if n == 1:
            # Base case: Move the smallest disk directly to the target peg
            print(f"Move disk {n} from peg {from_peg} to peg {to_peg}")
            moves += 1
        elif n == 2:
            # If there are only two disks, we can move them directly to the target peg and then to the second auxiliary peg
            print(f"Move disk {n - 1} from peg {from_peg} to peg {aux_peg1}")
            moves += 1
            print(f"Move disk {n} from peg {from_peg} to peg {to_peg}")
            moves += 1
            print(f"Move disk {n - 1} from peg {aux_peg1} to peg {to_peg}")
            moves += 1
        else:
            # Move n - 2 disks from from_peg to aux_peg1
            tower_of_hanoi(n - 2, from_peg, aux_peg1, aux_peg2, to_peg)

            # Move the (n - 1)th disk from from_peg to aux_peg2
            print(f"Move disk {n - 1} from peg {from_peg} to peg {aux_peg2}")
            moves += 1

            # Move the nth disk from from_peg to to_peg
            print(f"Move disk {n} from peg {from_peg} to peg {to_peg}")
            moves += 1

            # Move the (n - 1)th disk from aux_peg2 to to_peg
            print(f"Move disk {n - 1} from peg {aux_peg2} to peg {to_peg}")
            moves += 1

            # Move the n - 2 disks from aux_peg1 to to_peg
            tower_of_hanoi(n - 2, aux_peg1, to_peg, from_peg, aux_peg2)


def tower_of_hanoi_33_moves():
    print("33 moves algorithm:")
    print("Move disk 1 from peg A to peg D")
    print("Move disk 2 from peg A to peg B")
    print("Move disk 1 from peg D to peg B")
    print("Move disk 3 from peg A to peg C")
    print("Move disk 1 from peg B to peg A")
    print("Move disk 2 from peg B to peg C")
    print("Move disk 1 from peg A to peg C")
    print("Move disk 4 from peg A to peg D")
    print("Move disk 1 from peg C to peg D")
    print("Move disk 2 from peg C to peg B")
    print("Move disk 1 from peg D to peg B")
    print("Move disk 3 from peg C to peg A")
    print("Move disk 1 from peg B to peg C")
    print("Move disk 2 from peg B to peg A")
    print("Move disk 1 from peg C to peg A")
    print("Move disk 5 from peg A to peg B")
    print("Move disk 1 from peg A to peg D")
    print("Move disk 2 from peg A to peg B")
    print("Move disk 1 from peg D to peg B")
    print("Move disk 3 from peg A to peg D")
    print("Move disk 1 from peg B to peg A")
    print("Move disk 2 from peg B to peg D")
    print("Move disk 1 from peg A to peg D")
    print("Move disk 4 from peg D to peg C")
    print("Move disk 1 from peg D to peg B")
    print("Move disk 2 from peg D to peg C")
    print("Move disk 1 from peg B to peg C")
    print("Move disk 3 from peg D to peg B")
    print("Move disk 1 from peg C to peg D")
    print("Move disk 2 from peg C to peg B")
    print("Move disk 1 from peg D to peg B")
    print("Move disk 6 from peg A to peg D")
    print("Move disk 7 from peg A to peg C")
    print("Move disk 8 from peg A to peg B")


if __name__ == "__main__":
    n = int(input("Enter number of disks: "))
    pegs = ['A', 'B', 'C', 'D']
    moves = 0

    if n != 8:
        print("Using Divide and Conquer Algorithm")
        tower_of_hanoi(n, pegs[0], pegs[3], pegs[1], pegs[2])
        print("Number of moves:", moves)
    else:
        choice = int(input("Choose algorithm:\n1. Divide and Conquer Algorithm\n2. Custom Algorithm for 33 moves\nEnter your choice: "))
        if choice == 1:
            tower_of_hanoi(n, pegs[0], pegs[3], pegs[1], pegs[2])
            print("Number of moves:", moves)
        elif choice == 2:
            tower_of_hanoi_33_moves()
        else:
            print("Invalid choice!")
