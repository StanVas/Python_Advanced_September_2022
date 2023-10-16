# https://judge.softuni.org/Contests/Practice/Index/3515#1

from collections import deque

players = deque(input().split(', '))

SIZE = 6
matrix = []

for _ in range(SIZE):
    matrix.append(input().split())

skip_turn = {}
for pl in players:
    skip_turn[pl] = 0

while True:
    player = players.popleft()
    coordinates = input().strip('()').split(', ')
    row, col = [int(x) for x in coordinates]
    players.append(player)

    if skip_turn[player] > 0:
        skip_turn[player] -= 1
        continue

    if matrix[row][col] == "E":
        print(f"{player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == "T":
        print(f"{player} is out of the game! The winner is {players.popleft()}.")
        break

    elif matrix[row][col] == "W":
        skip_turn[player] += 1
        print(f"{player} hits a wall and needs to rest.")
        continue