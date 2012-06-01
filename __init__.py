
import sys
import os
import logging

RELATIVE_LIB_PATH = os.path.join('lib')

def add_lib_to_path():
    """
    Adds the SDK to the system path.
    """
    path = get_absolute_lib_path()
    sys.path.insert(0, path)


def get_absolute_lib_path():
    """
    Returns the absolute path of the SDK.

    @return: The path
    @rtype: str
    """
    path = os.path.join(__file__, '..', RELATIVE_LIB_PATH)
    return os.path.abspath(path)