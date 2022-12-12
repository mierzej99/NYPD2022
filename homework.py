import argparse
import json
import os
import tempfile
from typing import List, Union

import pytest

current_dir = os.path.dirname(__file__)


def take_from_list(li: list, indices: Union[int, List[int]]):
    """
    This function returns list of elements for given indices.

    :param li: list of elements
    :param indices: single index or list of indices
    :return: list of elements selected using indices
    """
    if isinstance(indices, int):
        indices = [indices]
    if not isinstance(indices, list) or not all(isinstance(i, int) for i in indices):
        raise ValueError(f"Indices should be integer or list of integers, not {type(indices)}")
    for index in indices:
        if index >= len(li):
            raise IndexError(f"Index {index} is to big for list of length {len(li)}")

    return [li[i] for i in indices]


def calculate(in_file: str, out_file: str):
    with open(in_file, 'r') as f_p:
        data = json.load(f_p)

    result = take_from_list(data["list"], data["indices"])

    with open(out_file, 'w') as f_p:
        json.dump(result, f_p)


@pytest.mark.parametrize('li,indices,res', [([], [], []), ([1, 2, 3], [], []), ([1, 2, 3], [0, 1, 2], [1, 2, 3])])
def test_take_from_list(li: list, indices: Union[int, List[int]], res: List[int]):
    assert take_from_list(li, indices) == res


def test_exceptions_take_from_list():
    with pytest.raises(IndexError):
        take_from_list([1, 2, 3], [4])
    with pytest.raises(ValueError):
        take_from_list([1, 2, 3], 'ungabunga')


@pytest.mark.parametrize(('content', 'res'),
                         [('{"list": [21, 96], "indices": [1]}', '[96]'), ('{"list": [21, 96], "indices": []}', '[]')])
def test_calculate(content: str, res: str, tmp_path):
    content = '{"list": [21, 96], "indices": [1]}'
    res = '[96]'

    d = tmp_path / "sub"
    d.mkdir()

    input_file = d / "input.json"
    input_file.write_text(content)

    output_file = d / "output.json"

    calculate(input_file, output_file)

    assert output_file.read_text() == res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", default=os.path.join(current_dir, "input.json"), nargs="?")
    parser.add_argument("output_file", default=os.path.join(current_dir, "output.json"), nargs="?")
    args = parser.parse_args()

    calculate(args.input_file, args.output_file)
