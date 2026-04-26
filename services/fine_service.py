def calculate_fine(extra_days):
    if extra_days <= 0:
        return 0

    fine = 0
    rate = 10

    for day in range(1, extra_days + 1):
        fine += rate * day

    return fine