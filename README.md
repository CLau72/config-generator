# Config File Generator

## Overview

FactoryTalk Network Manager uses FreeMarker templates in order to fill in values for switch configurations. This script is designed to read in a template file, determine the variables,
and generate individual configuration files. The goal is to make it so I only have to write one Stratix configuration, and then spit out one for every lab station I manage.

![DJ KHALED](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fimages%2Fba6509caf529c2d0f643e50e5a610c1a%2Ftenor.gif&f=1&nofb=1)

## Requirements

In order to use the script you need a couple pieces:

- **Template File**
    - The template file FTNM uses is a [FreeMarker Template](https://freemarker.apache.org/). Long story short, Any parameter in the config that needs to be replaced is of the format:

        ```ftl
        ${Parameter}
        ```
    - Templates live in the **templates** directory.
- **Inventory File**
    - This file is a .json file containing each station and the values for the parameters.

        ```json
        {
        "Station_00": {
            "${Hostname}": "SW-Demo",
            "${Gateway}": "192.168.1.1",
            "${VLAN}": "100"
            }
        }
        ```

    - The keys for the .json files match the parameter values in the template so it's easy to replace the values based on the keys.