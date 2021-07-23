#!/usr/bin/python3.9

from pathlib import Path
from core.numbers__ import fixed_set_precision_float
from time import sleep
from core.system import clearscreen

def get_CPU_percentage():
    cpu_system_file = Path("/proc/stat")
    contents = cpu_system_file.read_text()

    first_line = contents.split("\n")[0]

    items = first_line.split()[1:]
    #  print(items)

    items = list(map(int, items))

    idle = items[3]
    total_sum = sum(items)

    idle_percentage = (idle * 100) / total_sum
    idle_percentage = fixed_set_precision_float(idle_percentage, 2)
    #  print(idle_percentage)

    cpu_usage_percentage = 100 - idle_percentage
    
    return cpu_usage_percentage

while 1:
    #  clearscreen()
    print(get_CPU_percentage())
    sleep(1)
