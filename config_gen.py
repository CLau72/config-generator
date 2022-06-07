#!/usr/bin/env python3

# Script to take a FTNM style Stratix template and generate station specific outputs

import json
import os
import re
from simple_term_menu import TerminalMenu

# Select a file from the templates directory and return the file path
def file_select():
    files = os.listdir("./templates")
    terminal_menu = TerminalMenu(files)
    menu_entry_index = terminal_menu.show()
    return f"./templates/{files[menu_entry_index]}"


# Open the template file and read in each line
def parse_parameters(template_file):

    try:
        with open(template_file, encoding='UTF-8') as f:
            template = f.readlines()
    except:
        print("Unable to open template file")
    else:
    # Initialize empty list to add parameters to
        parameter_list = []

        # FTNM templates surround parameters with {$parameter}
        # Loop through the template and gather each instance of this structure
        for line in template:
            if re.search(r'\${.+}', line):
                parameter_list.append(re.search(r'\${.+}', line).group(0))

        # Take the list of paremeters collected from the template, and convert to a set to
        # get unique values
        parameters = set(parameter_list)
        return parameters


def generate_configs(template_file, inventory_file="inventory.json"):
    # Read in full file to get the template
    with open(template_file, mode="r") as f:
        template = f.read()
    # Obtain parameters based on template file
    parameters = parse_parameters(template_file)

    # Read in station inventory
    with open("inventory.json") as f:
        inventory = json.load(f)

    # For each station, replace all of the placeholder values with the actual values for that station based on inventory.json
    for station, values in inventory.items():
        with open(f"./output/{station}.txt", "w") as f:
            output = template
            for parameter in parameters:
                output = output.replace(parameter, values[parameter])
            f.write(output)


def main():

    template_file = file_select()
    generate_configs(template_file)


if __name__  == "__main__":
    main()

