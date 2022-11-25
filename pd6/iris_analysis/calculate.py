import statistics as stat


def calculate_mean(values):
    return stat.mean(values)


def calculate_median(values):
    return stat.median(values)


def calculate_std(values):
    return stat.stdev(values)


def calculate_metric_for_matrix(iris):
    metrics = dict()
    for name in iris.keys():
        metrics[name] = [f(iris[name]) for f in (calculate_mean, calculate_mean, calculate_std)]
    return metrics
