'''Task5_1. Open file `data/unsorted_names.txt` in data folder.
 Sort the names and write them to a new file called `sorted_names.txt`.
 Each name should start with a new line '''

import data
file = open("data/unsorted_names.txt", "r")

sorted_names = sorted(file.readlines())
file.close()

file = open("data/sorted_names.txt", "w")
for name in sorted_names:
    file.write(name)
file.close()
