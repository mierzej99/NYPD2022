import numpy as np



if __name__ == '__main__':
    arr = np.load('ex3_data.npy')
    number_of_nan = np.sum(np.isnan(arr))
    number_of_rows_with_nan = np.sum(np.isnan(arr).any(axis=1))
    number_of_nan_in_columns = []
    for i in range(arr.shape[1]):
        number_of_nan_in_columns += [np.sum(np.isnan(arr[:,i]))]
    print(number_of_nan_in_columns)