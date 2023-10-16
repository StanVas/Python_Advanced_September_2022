SIZE = 6

matrix = []

for _ in range(SIZE):
    matrix.append(input().split())

score = 0

for _ in range(3):
    row, col = [int(x) for x in input().strip('()').split(', ')]
    if row < SIZE and col < SIZE:
        if matrix[row][col] == "B":
            matrix[row][col] = 0
            for row in range(SIZE):
                score += int(matrix[row][col])

if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
else:
    prize = ''
    if 100 <= score <= 199:
        prize = 'Football'
    elif 200 <= score <= 299:
        prize = 'Teddy Bear'
    elif score >= 300:
        prize = 'Lego Construction Set'
    print(f"Good job! You scored {score} points, and you've won {prize}.")
