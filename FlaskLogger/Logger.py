from logging.config import fileConfig
import yaml


def yamlparser(log_path):
    with open(log_path) as f:
        result =  yaml.safe_load(f)
    return result


fileConfig('logging.cfg')