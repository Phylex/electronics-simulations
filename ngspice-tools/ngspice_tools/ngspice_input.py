"""
Module containing functions to read in data from ngspice output
"""
from typing import List, TextIO, Tuple


def parse_ngspice_sim_output(file: TextIO) -> Tuple[str, str, List[str]]:
    """
    Parse the file created by the ngspice write command
    and return the data and metadata
    """
    line_1 = file.readline()
    line_2 = file.readline()
    line_3 = file.readline()
    title = " ".join(line_3.split(" ")[1:] + ["of"] + line_1.split(" ")[1:])
    date = " ".join(line_2.split(" ")[1:])
    del line_1
    del line_2
    del line_3
    file.readline()
    number_of_variables = int(file.readline().split(" ")[-1])
    number_of_points = int(file.readline().split(" ")[-1])
    simvars = []
    file.readline()
    for _ in range(number_of_variables):
        var_name_line = file.readline().split("\t")
        var_name = var_name_line[-2].strip()
        var_type = var_name_line[-1].strip()
        if var_type == "time":
            var_unit = "[s]"
        elif var_type.lower() == "voltage":
            var_unit = "[V]"
        elif var_type.lower() == "current":
            var_unit = "[I]"
        else:
            var_unit = "unknown unit"
        simvars.append({'name': var_name, 'type': var_type,
                       'unit': var_unit, 'data': []})
    file.readline()
    for _ in range(number_of_points):
        for i in range(number_of_variables):
            tokens = file.readline().split("\t")
            simvars[i]['data'].append(
                float(tokens[-1][:-1]))
        file.readline()
    return title, date, simvars
