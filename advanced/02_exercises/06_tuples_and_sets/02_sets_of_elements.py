lines = list(map(int, input().split()))
n_line = lines[0]
m_line = lines[1]
n_set = set()
m_set = set()

for num in range(n_line):
    number = int(input())
    n_set.add(number)

for num in range(m_line):
    number = int(input())
    m_set.add(number)

intersection = n_set.intersection(m_set)
for element in intersection:
    print(element)
