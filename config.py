import yaml

with open("config/data_files.yml") as config:
    config = yaml.load(config.read())

file_paths = map(
    lambda name: "{0}/{1}".format(config["path"], name),
    config["file_names"])

