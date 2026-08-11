def natural_sum(n):
    if n == 0:
        return 0
    return n + natural_sum(n-1)
