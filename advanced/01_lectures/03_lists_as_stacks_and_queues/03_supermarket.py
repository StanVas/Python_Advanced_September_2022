from collections import deque

supermarket_queue = deque()

while True:
    client = input()
    if client == 'End':
        print(f'{len(supermarket_queue)} people remaining.')
        break

    elif client == 'Paid':
        print('\n'.join(supermarket_queue))
        supermarket_queue.clear()

    else:
        supermarket_queue.append(client)
