import random

def objective_function(x):
    return -(x - 3) **2 + 9

def hill_climb(start_x, step_size=0.1, max_iteration=100):
    current_x = start_x
    current_value= objective_function(current_x)

    for _ in range (max_iteration):
        next_x = current_x + random.choice([-step_size, step_size])
        next_value = objective_function(next_x)

        if next_value > current_value:
            current_x, current_value = next_x, next_value
        else:
            break
    
    return current_x, current_value

start_x= random.uniform(0,6)
best_x, best_value = hill_climb(start_x)

print(f"Best x found: {best_x:2f}, Maximum value: {best_value:2f}")
