from astar import a_star_search

N = 3  # Αριθμός ιεραποστόλων και κανιβάλων
M = 4# Χωρητικότητα βάρκας
K = 50  # Μέγιστος αριθμός διασχίσεων

solution_path = a_star_search(N, M, K)

if solution_path:
    print("Λύση βρέθηκε σε", len(solution_path), "βήματα:")
    for state in solution_path:
        print(f"Μ: {state.missionaries_left}, Κ: {state.cannibals_left}, Βάρκα: {'Αριστερά' if state.boat_position == 0 else 'Δεξιά'}")
else:
    print("Δεν βρέθηκε λύση εντός του ορίου διασχίσεων.")
