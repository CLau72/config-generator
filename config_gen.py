#!/usr/bin/env python3

# Script to take a FTNM style Stratix template and generate station specific outputs

import re

# Open the template file and read in each line
with open('template.txt', encoding='UTF-8') as f:
    output = f.readlines()

# Initialize empty list to add parameters to
parameter_list = []

# FTNM templates surround parameters with {$parameter}
# Loop through the template and gather each instance of this structure
for line in output:
    if re.search(r'\${.+}', line):
        parameter_list.append(re.search(r'\${.+}', line).group(0))

# Take the list of paremeters collected from the template, and convert to a set to
# get unique values
parameters = set(parameter_list)

print(parameters)