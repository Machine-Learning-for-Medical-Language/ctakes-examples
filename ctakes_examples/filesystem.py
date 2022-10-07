"""File reading methods"""

import glob
import os
from typing import List


###############################################################################
#
# Reading all tests
#
###############################################################################

def list_curated() -> List[str]:
    """
    Return filenames for all curated examples.

    There is no personal health information (PHI) in these examples.
    They were manually created without reference to real patients.

    :return: list of curated example files
    """
    return _list_examples('curated')


def list_synthetic() -> List[str]:
    """
    Return filenames for all synthetic examples.

    There is no personal health information (PHI) in these examples.
    They were automatically generated without reference to real patients.

    :return: list of sythetic example files
    """
    return _list_examples('synthetic')


###############################################################################
#
# Reading specific tests
#
###############################################################################

def read_curated(name: str) -> str:
    """
    Returns note contents for the given curated example

    There is no personal health information (PHI) in these examples.
    They were manually created without reference to real patients.
    """
    return _read_example('curated', name + '.txt')


def read_synthetic(name: str) -> str:
    """
    Returns note contents for the given synthetic example

    There is no personal health information (PHI) in these examples.
    They were automatically generated without reference to real patients.
    """
    return _read_example('synthetic', name + '.txt')


###############################################################################
#
# Helpers
#
###############################################################################

def _example_dir(example_type: str) -> str:
    """Returns path to locally shipped resources for the given example type"""
    return os.path.join(os.path.dirname(__file__), 'resources', example_type)


def _list_examples(example_type: str) -> List[str]:
    """
    Returns all example file paths for a given example type

    The results are sorted by filename.
    """
    glob_pattern = os.path.join(_example_dir(example_type), '*.txt')
    return sorted(glob.glob(glob_pattern))


def _read_example(example_type: str, filename: str) -> str:
    """
    Opens a given example file and returns a file-like object
    """
    return open(os.path.join(_example_dir(example_type), filename), 'r', encoding='utf8').read()
