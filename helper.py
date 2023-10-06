"""
A collection of helper methods
"""

import os


def return_path():

    # inp1 = input(f"Please input location path of group shift stats: ")

    inp1 = r"C:\Users\Angel\Downloads\group_stats_detailed_164259_90sxeijc97.xlsx"

    path1 = os.path.abspath(inp1.strip(' \"'))
    return fr"{path1}"
