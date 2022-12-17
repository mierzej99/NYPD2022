import numpy as np


def zad3(file):
    arr = np.load(file)
    number_of_nan = np.sum(np.isnan(arr))
    number_of_rows_with_nan = np.sum(np.isnan(arr).any(axis=1))
    number_of_nan_in_columns = []
    for i in range(arr.shape[1]):
        number_of_nan_in_columns += [np.sum(np.isnan(arr[:, i]))]

    arr = arr[~np.isnan(arr).any(axis=1)]

    return {'Ile jest nan':number_of_nan, 'ile jest wierszy z nan':number_of_rows_with_nan, 'ile jest nan w kazdej kolumnie':number_of_nan_in_columns, 'maciersz po filtrowaniu':arr}


if __name__ == '__main__':
    print(zad3('ex3_data.npy'))
