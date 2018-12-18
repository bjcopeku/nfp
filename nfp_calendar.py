#   5    5    5    20   5    5    5    40   5    5    5    60   5    72|    5   |80   5    5    5    5    5    5
# GOALS:
# 1.  Add list of imported files - DONE
# 2.  Add function to check if imported - DONE
# 3.  Not sure I have correctly handled missing data, but think so - DONE
# 4.  Way to handle corrupted location and category entries
# 5.  Delete/edit location, category
# 6.  Delete/edit bad individual transaction
# 7.  Currently nothing catches for a known location + group location w/o known category for that group location
# 8.  Check for duplicate data

import csv
# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

# from urllib.request import Request, urlopen
# from urllib.error import HTTPError
# from urllib.parse import urlencode

# global variables:
calendar_data = []
x_values = []
y_values = []

plotting_data = {}


# I think I will need this
class Month:
    pass


# class to hold the user data for a standard day
class Day:
    def __init__(self, row):
        self._date = row[0]
        # x_values.append(row[0])
        self._new_cycle = row[1]

        if row[2] == '-':
            self._temperature = 0
        else:
            self._temperature = float(row[2])
        # y_values.append(row[2])

        plotting_data[len(plotting_data)] = self._temperature

        self._questionable_temp = row[3]
        self._fluid_sticky = row[4]
        self._fluid_creamy = row[5]
        self._fluid_eggwhite = row[6]
        self._fluid_watery = row[7]
        self._cervix_height = row[8]
        self._cervix_openness = row[9]
        self._cervix_firmness = row[10]
        self._opk = row[11]
        self._preg_test = row[12]
        self._menstruation = row[13]
        self._spotting = row[14]
        self._sex = row[15]
        self._peak_day = row[16]
        self._temperature_shift = row[17]
        self._custom = row[18]
        self._notes = row[19]

    def print_data(self):
        return f"Day: {self._date} and temp: {self._temperature}"

    def get_plot_data(self):
        return self._date, self._temperature


def get_lowest_temp_line(temps):
    for i in temps:
        if i + 13 == len(temps):
            plt.text(15, 99, "Cannot apply the ST Rule", horizontalalignment='center',
                     verticalalignment='center', fontsize=10, bbox=dict(facecolor='red', alpha=0.5))
            return

        temp_max = max((temps[i + 5] + 0.1), (temps[i + 6] + 0.1), (temps[i + 7] + 0.1),
                       (temps[i + 8] + 0.1), (temps[i + 9] + 0.1), (temps[i + 10] + 0.1))
        if (temps[i + 11] >= temp_max) and (temps[i + 12] >= temp_max) and (temps[i + 13] >= temp_max):
            print("value of line: ", temps[i + 11], temps[i + 12], temps[i + 13], " is greater than: ", temps[i + 5],
                  temps[i + 6], temps[i + 7], temps[i + 8], temps[i + 9], temps[i + 10])
            # draw the LTL in red
            plt.axhline(y=temps[i + 11], color='r')
            # draw the HTL in green
            plt.axhline(y=temps[i + 11] + 0.4, color='g')
            return


# reads the data file line by line, parsed by comma, and calls 'Day' for each line
with open("test_data.csv", 'r') as calendar_file:
    reader = csv.reader(calendar_file, delimiter=',')
    headers = next(reader)
    for line in reader:
        calendar_data.append(Day(line))  # adds a new Day object to the list

if __name__ == "__main__":

    plt.xlabel('Cycle Day')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.axis([0, len(plotting_data), 95.5, 99.5])
    for k, v in plotting_data.items():
        plt.plot(k, v, 'bo')
    # LTline = get_lowest_temp_line(plotting_data)
    # plt.axhline(y=LTline, color='r')
    # plt.axhline(y=LTline+0.4, color='r')
    get_lowest_temp_line(plotting_data)
    plt.text(15, 98, "Cannot apply the ST Rule", horizontalalignment='center',
             verticalalignment='center', fontsize=30, bbox=dict(facecolor='red', alpha=0.5))
    plt.show()

# format for printing the data to a file
# with open("Locations.csv", 'w', newline='') as csvfile:
#     fieldnames = ['statement', 'grouping']
#     w = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     w.writeheader()
#     for key,value in bank_locations_dict.items():
#         # print(key, "corresponds to", d[key])
#         w.writerow({'statement' : key, 'grouping' : bank_locations_dict[key]})
