# problem-solving-using-python

## 1) Inverting a Coin Triangle

**Question:**
Consider an equilateral triangle formed by closely packed pennies or other identical coins. Use iterative improvement method to design an algorithm to flip the triangle upside down in the minimum number of moves if on each move you can slide one coin at a time to its new position.

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/bceeda6d-4baf-48f6-bc14-f6c1fee22371)

**Files:**
- `coin_triangle.py`: Contains the implementation of the algorithm to flip the coin triangle upside down.

**Description:**
In this file, I've implemented an iterative algorithm that flips an equilateral triangle formed by closely packed identical coins upside down using the minimum number of moves. Each move involves sliding one coin at a time to its new position. The triangle is initially positioned with its base on the bottom and apex on the top. My objective here is to invert the triangle so that the base becomes the top and the apex becomes the bottom. I've considered the closely packed nature of the coins and devised a strategy to efficiently flip the triangle while ensuring that only one coin is moved at a time.


**TEST Example:**

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/c2c7e310-2df6-4e72-a959-e8b354447a60)


## 2) Peg Solitaire

**Question:**
Consider the one-dimensional version of peg solitaire played on an array of n cells. Write an algorithm that removes all but one peg by a sequence of moves and finds all the locations of the empty cell in the initial setup for which the puzzle can be solved.

**Files:**
- `peg_solitaire.py`: Contains the implementation of the algorithm to solve peg solitaire.

**Description:**
I've implemented two algorithms for solving one-dimensional peg solitaire using brute force.

- Algorithm for removing all but one peg: I iterate through all possible moves, simulating each to find a sequence where only one peg remains.

- Algorithm for finding all solvable configurations: I identify all empty cell locations where the puzzle can be solved by iterating through configurations and simulating moves.

**Test Example:**
**The current setup yielded no feasible solution.**

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/0906f17e-d658-4866-a3df-2560e94863de)

**This setup’s output was:[0 0 0 0 1 0] which is a feasible solution.**

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/6db8e0a0-7948-4ab3-92b6-0544bebd13ec)

**This setup uses an array with four elements and solution [0 1 0 0] was given**

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/6fc654d8-cfee-4088-963e-b7ba24a18102)



## 3) Knights Exchange

**Question:**
There are six knights on a 3 × 4 chessboard. Design an iterative improvement algorithm to exchange the knights to get the specified position in the minimum number of moves, not allowing more than one knight on a square at any time.

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/4263e250-f6f0-4f24-b377-daa0848ca5ef)

**Files:**
- `knights_exchange.py`: Contains the implementation of the algorithm to exchange the knights.

**Description:**
I've implemented an algorithm using an iterative improvement combined with a greedy approach to exchange the knights on a 3x4 chessboard.

- Algorithm for knight exchange: I've designed an algorithm that iteratively improves the position of the knights on the chessboard, following the rules of chess. The goal is to reach a specific configuration where each square on the chessboard has at most one knight, with the minimum number of knight moves.
  
- Greedy approach: In addition to the iterative improvement, I've incorporated a greedy approach to make locally optimal choices at each step, aiming to minimize the number of knight moves required to achieve the desired configuration.


**TEST example:**

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/e01dcf7a-3efc-411c-8801-700f7376e666)


## 4) Penny Machine

**Question:**
A “machine” consists of a row of boxes. Design an algorithm using Brute Force method to automate the machine and answer questions about its behavior.

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/c8906fa4-dc23-4a6b-8152-270f579232d4)

**Files:**
- `penny_machine.py`: Contains the implementation of the algorithm to automate the penny machine.

**Description:**
I've implemented an algorithm to automate the operation of a penny redistribution machine.

Algorithm for penny redistribution: The algorithm begins by placing n pennies in the leftmost box and then proceeds to redistribute the pennies according to the rules of the machine. It iteratively replaces pairs of pennies in one box with a single penny in the next box to the right, selecting pairs from the leftmost box with at least two pennies on each iteration. The process continues until no box contains more than one penny.


**TEST example 1:**

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/4bc2d938-d585-4277-8aee-4ec874357aa6)

**detailed explanation:**


![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/9698528a-5d51-4082-8897-f2a3b185e125)

**TEST example 2:**


![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/82fd9e89-f45a-47e5-9070-8b060cbc85f1)

**detailed explanation:**


![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/1cc70756-b35a-4b65-b368-7c71fc44a7b8)


## 5) Security Switches

**Question:**
There is a row of n security switches protecting a military installation entrance. Design a Divide and Conquer algorithm to turn off all the switches in the minimum number of moves.

**Files:**
- `security_switches.py`: Contains the implementation of the Divide and Conquer algorithm for turning off the switches.

**Description:**
I've implemented a Divide and Conquer algorithm to turn off all the switches, which are initially all on, in the minimum number of moves.

Algorithm for switch toggling: The algorithm follows a Divide and Conquer approach to efficiently toggle the switches. It begins by identifying the rightmost switch and toggles it as needed. Then, it recursively divides the remaining switches into subproblems and toggles them based on the given rules: any switch may be turned on or off only if the switch to its immediate right is on and all the other switches to its right, if any, are off. Only one switch may be toggled at a time.

Objective: The goal is to find the minimum number of moves required to turn off all the switches. Each toggling action counts as one move.


**TEST example:**


![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/31d8c250-386b-418b-966a-96d3c61faf32)



## 6) Tower of Hanoi

**Question:**
Use divide and conquer method to transfer all the disks from one peg to another peg.


**Files:**
- `tower_of_hanoi.py`: Contains the implementation of the Tower of Hanoi puzzle solver.

**Description:**
I've implemented an algorithm to solve the Tower of Hanoi puzzle using the divide and conquer method.

Algorithm for Tower of Hanoi: The algorithm begins with all eight disks placed on the first peg in order of size, with the largest disk at the bottom and the smallest at the top. It then recursively divides the problem into subproblems, moving one disk at a time to achieve the goal of transferring all disks to another peg while adhering to the rules: only one disk can be moved at a time, and it is forbidden to place a larger disk on top of a smaller one.

Objective: The goal is to determine if the divide and conquer algorithm can solve the puzzle in 33 moves. If not, the algorithm will be redesigned to achieve the solution in 33 moves.


**Test Example:**

![image](https://github.com/nouran555/problem-solving-using-python/assets/129008133/a30c9294-8c4d-4b0d-b54e-3e450080de2e)






