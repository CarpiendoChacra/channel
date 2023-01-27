import os
from typing import List
import yaml

languages = {}
commands = {}

def get_command(value: str) -> List:
    return commands["command"][value]

def get_string(lang: str):
    return languages[lang]

for filename in os.listdir(r"./lang"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./lang/" + filename, encoding="utf8")
        )

for filename in os.listdir(r"./lang/langs/"):
    if "es" not in languages:
        languages["es"] = yaml.safe_load(
            open(r"./lang/langs/en.yml", encoding="utf8")
        )
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "es":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./lang/langs/" + filename, encoding="utf8")
        )
        for item in languages["es"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["es"][item]