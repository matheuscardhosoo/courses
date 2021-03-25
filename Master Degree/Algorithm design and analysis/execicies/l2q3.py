"""
List 2 - Question 3

Given the following abstraction:
- Group with the trucks: T = {t1, t2, ..., tn}.
    - With capacity: C = {c1, c2, ..., cn}.
- Group with the items: G = {g1, g2, ..., gn}.
    - With weight: W = {w1, w2, ..., wn}.
    - With value: V = {v1, v2, ..., vn}.

So, we have the following recorrency for dynamic programming:
- If (c1 < w(i)) and ... and (cj < w(i)) and ... and (cn < w(i)):
    - OPT(i, c1,...,cj,...,cn) = OPT(i-1, c1,...,cj,...,cn)
- if (cj - w1) >= 0:
    - OPT(i, c1,...,cj,...,cn) = MAX{OPT(i-1, c1,...,cj,...,cn)
                                     v(i) + OPT(i-1, c1-w(i),...,cj,...,cn), ...,
                                     v(i) + OPT(i-1, c1,...,cj-w(i),...,cn), ...,
                                     v(i) + OPT(i-1, c1,...,cj,...,cn-w(i))}
"""
import numpy as np


def how_much_was_lost(trucks_capacities, items_weights, items_values):
    trucks_count = len(trucks_capacities)
    items_count = len(items_values)
    # OPT function

    def opt(i, *current):
        if i < 0:
            return 0
        partial = [opt(i-1, *current)]
        for t in range(trucks_count):
            if current[t] >= items_weights[i]:
                adjust = np.array(current)
                adjust[t] = adjust[t] - items_weights[i]
                partial.append(opt(i-1, *adjust) + items_values[i])
        return max(partial)
    #
    return sum(items_values) - opt(items_count - 1, *trucks_capacities)


trucks_capacities = [5, 4, 3]
items_weights = [1, 2, 4, 4, 4, 2, 1]
items_values = [1, 2, 3, 4, 3, 2, 1]
print(how_much_was_lost(trucks_capacities, items_weights, items_values))
