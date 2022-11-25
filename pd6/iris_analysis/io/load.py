import csv


def load_file(path_to_file):
    with open(path_to_file, 'r') as f:
        lines = list(csv.reader(f, delimiter=','))
    for i, _ in enumerate(lines):
        lines[i] = lines[i][:-1]
    iris = dict()
    for i, name in enumerate(lines[0]):
        iris[name] = [float(x[i]) for x in lines[1:]]
    return iris
