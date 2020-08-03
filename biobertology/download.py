"""Usage:
          get_weights.py [--dir=<dataset-name>]

@ Jevgenij Gamper 2020
Downloads biobert v1.1 (+pubmed 1m) weights into a specified location. If location is not specified will attempt to
download into default path ~/.biobertology/biobert_v1.1_pubmed

Options:
  -h --help                       Show help.
  --version                       Show version.
  --dir=<dir>                     Name of the dataset to be downloaded
"""
from docopt import docopt
import os
from os.path import expanduser
import wget
import shutil


LINK = "https://www.dropbox.com/s/dc2ki2d4jv8isrb/biobert_weights.zip?dl=1"


def get_default_biobert_path():
    """
    :return: path "/home/user_name/.biobertology
    """
    home_dir_path = expanduser("~")
    return os.path.join(home_dir_path, ".biobertology")


def download_and_extract(target_directory):
    """
    Downloads and extracts biobert weights
    :return:
    """
    # Make sure that directory for pannuke exists
    os.makedirs(target_directory, exist_ok=True)
    wget.download(LINK, out=target_directory)
    downloaded_file_path = os.path.join(target_directory, "biobert_weights.zip")
    shutil.unpack_archive(downloaded_file_path, target_directory)
    os.remove(downloaded_file_path)


def parse_arguments(arguments):
    user_directory = arguments["--dir"]
    target_directory = user_directory if user_directory else get_default_biobert_path()
    return target_directory


if __name__ == "__main__":
    arguments = docopt(__doc__)
    target_directory = parse_arguments(arguments)
    download_and_extract(target_directory)
