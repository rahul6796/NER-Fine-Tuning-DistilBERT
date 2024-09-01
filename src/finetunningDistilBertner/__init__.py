


import os

from src.finetunningDistilBertner.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import yaml






@ensure_annotations
def read_yaml(path_of_yaml: Path, verbose = True) -> ConfigBox:
    try:
        with open(path_of_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml_path : {yaml_file} load successfully !')
            return ConfigBox(content)


    except Exception as e:
        logger.error(f'raised error from read yaml :: {e}')


@ensure_annotations
def create_directories(path_of_directories: list, verbose =True):
    try:
        for path in path_of_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'directory created :: {path}')
    except Exception as e:
        logger.error(f'error raised from create directoris :: {e}') 



@ensure_annotations
def get_size(path: Path) -> int:
    """
    this method return the size of file.

    Args:
        path: input like path.
    Returns:
        size: size of file.
    """
    try:
        size_in_kb = os.path.getsize(path/1024)
        return f"~ size in{size_in_kb} kb"
    except Exception as e:
        logger.error(f'error is raised from get size function :; {e}')
