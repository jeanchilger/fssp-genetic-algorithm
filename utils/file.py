import numpy as np
import shutil
from typing import Union
from pathlib import Path


# def _get_path(path: Union[str, Path]) -> Path:
#     """
#     Produces a Path object for the given string path.
#     If input is already a Path object, returns it.
#     Args:
#         path (Union[str, Path]): A path representation,
#             string or Path object.
#     Returns:
#         Path: Path object.
#     """

#     if type(path) == str:
#         return Path(path.replace("\\", "/"))
    
#     return path


# def create_dir(path: Union[str, Path]) -> None:
#     """
#     Creates a folder, if not exists, at the given location.
#     Parent folders that don't exists are also created.
#     Args:
#         path (Union[str, Path]): Path to create a new directory.
#     """

#     _path = _get_path(path)

#     if not _path.exists():
#         _path.mkdir(parents=True)


# def create_file(path: Union[str, Path]) -> None:
#     """
#     Creates an empty file at the given location.
#     Args:
#         path (Union[str, Path]): Path where the file should be created.
#     """

#     _path = _get_path(path)
#     _path.touch()

def get_instance_from_file(input_path: Union[str, Path]) -> np.ndarray:
    """
    Generator function that returns the instances in a file.

    Args:
        input_path (Union[str, Path]): Path to the instace file.

    Returns:
        np.ndarray: A matrix representing a single instance.
    """
    
    skip_count = 0
    n_machines = _get_num_machines(input_path)
    instance = []

    with open(input_path, 'r') as txt_file:
        for row in txt_file:
            skip_count += 1
            
            if 0 < skip_count % (n_machines + 3) <= 3:
                instance = []
                continue
            
            instance.append(list(map(int, row.strip().split())))
            
            if len(instance) == n_machines:
                yield np.array(instance, dtype=np.int32)

def _get_num_machines(input_file_name: str) -> int:
    """
    Returns the number of machines from the name of the input file.

    Args:
        input_file_name (str): Input file name.

    Returns:
        int: Number of machines.
    """
    
    return int(input_file_name.split('.')[0].split('_')[-1])

# def is_path(path: Union[str, Path]) -> bool:
#     """
#     Returns whether or not the given path is a valid path.
#     To be valid, a path must lead to an existing location
#     and can't be an arbitrary text string.
#     Args:
#         path (Union[str, Path]): Path to check validity
#     Returns:
#         bool: True if given path is valid. False otherwise.
#     """
    
#     try:
#         return _get_path(path).exists()
#     except:
#         return False


# def read_txt_file(path: Union[str, Path]) -> str:
#     """
#     Reads a file as plain text, returning the contents as a string.
#     Args:
#         path (Union[str, Path]): Path to file.
#     Returns:
#         str: File contents as plain text.
#     """
    
#     _path = _get_path(path)
    
#     with open(_path, "r") as txt_file:
#         return txt_file.read().strip()


# def write_txt_file(path: Union[str, Path], content: str) -> None:
#     """
#     Writes the given content to the file at given location
#     as plain text.
#     Args:
#         path (Union[str, Path]): Path to file.
#         content (str): Text to write to file.
#     """
    
#     _path = _get_path(path)
    
#     with open(_path, "w") as txt_file:
#         txt_file.write(content)