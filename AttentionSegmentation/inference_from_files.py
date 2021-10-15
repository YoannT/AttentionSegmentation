from __future__ import absolute_import
import argparse
import sys
import json

from AttentionSegmentation.model.inference import BasicAttentionModelRunner
from AttentionSegmentation.commons.utils import setup_logger


def get_arguments():
    parser = argparse.ArgumentParser(description="Time Tagger")
    parser.add_argument('-bd', '--base_dir', action="store",
                        dest="base_dir", type=str,
                        help="path to the experiment directory", required=True)
    parser.add_argument('-vf', '--val_file', action="store", dest="val_file",
                        type=str, help="The test file", required=True)
    parser.add_argument('-hf', '--html_file', action="store", dest="html_file",
                        type=str, default="",
                        help="The html file used for output")
    parser.add_argument("-pf", "--pred_file", action="store", dest="pred_file",
                        type=str, default="",
                        help="The prediction json file")
    parser.add_argument("-tol", "--tol", action="store", dest="tol",
                        type=float, default=0.01,
                        help="Attention threshold tolerance")
    args = parser.parse_args(sys.argv[1:])
    return args


if __name__ == "__main__":
    setup_logger()
    args = get_arguments()
    base_dir = args.base_dir
    runner = BasicAttentionModelRunner.load_from_dir(base_dir)
    valid_file = args.val_file
    visualization_file = args.html_file
    prediction_file = args.pred_file
    predictions = runner.generate_preds_from_file(
        valid_file, prediction_file, visualization_file)
