def mean(data):
    return sum(data) / len(data)

def median(data):
    n = len(data)
    sorted_data = sorted(data)

    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]