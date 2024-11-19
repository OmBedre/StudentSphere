class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.cost = value / weight  # Cost per weight unit


def fractional_knapsack(capacity, items):

    items.sort(key=lambda item: item.cost, reverse=True)

    total_value = 0

    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:

            total_value += item.value
            capacity -= item.weight
        else:

            total_value += item.cost * capacity
            capacity = 0

    return total_value



if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []

    for _ in range(n):
        value = float(input("Enter the value of the item: "))
        weight = float(input("Enter the weight of the item: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))

    max_value = fractional_knapsack(capacity, items)
    print("Maximum value in the knapsack:", max_value)