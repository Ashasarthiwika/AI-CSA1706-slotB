from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0:
        return False

    if m_right < 0 or c_right < 0:
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = {start}

    moves = [
        (1, 0), (2, 0),
        (0, 1), (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution:")
            for step in path + [state]:
                print(step)
            return

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if new_state not in visited and is_valid(new_state[0], new_state[1]):
                visited.add(new_state)
                queue.append((new_state, path + [state]))

solve()
