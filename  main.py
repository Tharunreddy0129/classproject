# main.py
import yaml
from file_utils import read_file

# Read config file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Read source file
source_content = read_file(config['source_file'])

# Copy source content to destination file
with open(config['destination_file'], 'w') as file:
    file.write(source_content)
