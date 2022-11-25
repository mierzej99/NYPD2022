import iris_analysis
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input_file", help="path to input file", required=True
    )
    parser.add_argument(
        "-o", "--result_file", help="path to output file", required=True
    )

    args = parser.parse_args()

    data = iris_analysis.io.load.load_file(args.input_file)
    metrics = iris_analysis.calculate.calculate_metric_for_matrix(data)
    iris_analysis.io.save.save_file(args.result_file, metrics)
