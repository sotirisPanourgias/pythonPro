import heapq

from state import State


def a_star_search(N, M, K):
    initial_state = State(N, N, 0, 0)
    initial_state.evaluate(N,M)

    open_set = []
    closed_set = set()

    heapq.heappush(open_set, (initial_state.f, initial_state))

    while open_set:
        _, current_state = heapq.heappop(open_set)

        if current_state.is_final():
            return reconstruct_path(current_state)

        closed_set.add(current_state)

        for child in current_state.get_children(N):
            if child in closed_set:
                continue

            child.g = current_state.g + 1
            child.evaluate(N,M)


            if child.g > K:
                continue


            heapq.heappush(open_set, (child.f, child))

    return None


def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.father
    return path[::-1]
