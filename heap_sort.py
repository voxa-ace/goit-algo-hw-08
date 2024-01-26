import heapq

def min_cost_to_combine_cables(cable_lengths):
    """
    Calculate the minimum cost to combine all the given network cables.

    This function uses a min heap to efficiently combine the cables in pairs,
    always taking the two shortest available cables to minimize the cost.

    Parameters:
    cable_lengths (list of int): A list of cable lengths.

    Returns:
    int: The minimum cost to combine all the cables, or 0 if the list is empty.
    """
    if not cable_lengths:  # Check if the list is empty
        return 0

    # Initialize a min heap with the given cable lengths
    heapq.heapify(cable_lengths)
    total_cost = 0

    # Continue combining cables until only one cable remains
    while len(cable_lengths) > 1:
        # Pop the two shortest cables
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Combine them and add the cost
        combined = first + second
        total_cost += combined

        # Push the combined cable back into the heap
        heapq.heappush(cable_lengths, combined)

    return total_cost

# Example usage
cable_lengths = [5, 2, 4, 6, 7, 3]
print("Minimum cost to combine all cables:", min_cost_to_combine_cables(cable_lengths))
