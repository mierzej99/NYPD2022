import csv


def save_file(path_to_file, results):
    with open(path_to_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(results.keys())
        for i in range(len(list(results.values())[0])):
            writer.writerow([results[name][i] for name in results.keys()])
