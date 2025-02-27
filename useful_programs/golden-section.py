"""
function GoldenSectionSearch(f, a, b, tol):
    phi = (1 + sqrt(5)) / 2       # Golden ratio
    resphi = 2 - phi              # 1 / phi, approximately 0.61803

    # Calculate initial points
    c = b - resphi * (b - a)
    d = a + resphi * (b - a)

    while (b - a) > tol:
        if f(c) < f(d):
            b = d                # Move the upper bound
            d = c                # Update d
            c = b - resphi * (b - a)
        else:
            a = c                # Move the lower bound
            c = d                # Update c
            d = a + resphi * (b - a)

    # Return the midpoint of the final interval
    return (a + b) / 2

"""