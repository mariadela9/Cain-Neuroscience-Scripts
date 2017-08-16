import os
# Csv module that allows manipulation of csv files
import csv
"""

Takes all of the csv files in a directory and takes certain cells and transposes
them onto rows of a new csv file

"""
#  Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd
#  Change directory to where all of the csv files are located
#  Comment out if the script is located under the directory containing all files
os.chdir("/Users/ferdela/Developer/Cain_Lab/data/final_data")

#  Initialize the field that will contain all of the rows to be
#  later written on the new file
all_rows = []

#  Initialize the title fields that will be on the first line of the new file,
#  you can either do this manually or open a file and get the first line as below

#  Example: first line of existing file - uncomment below

# # Opens the any file containing the titles
# # First argument is the file's name
# #  Second argument is the mode to open file, in this case 'r' is read
# with open(file_containing_titles, 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
#
#     # extracting field names through first row
#     fields = next(csvreader)

# Example: manually input first row titles
fields = ['RatID',
          'Video Title',
          'Response Start Time',
          'Scorer Initials',
          'Locomotion:',
          'Out of View Time',
        'Mouth Movements',
        'Tongue protrusions',
        'Lateral tongue protrusions',
        'Paw lickings',
        'Lip flair/Smacks',
        'Gapes',
        'Head shakes',
        'Forelimb flails',
        'Paw-pushings',
        'Chin rubs',
        'Fluid expulsions',
        'Grooms',
        'Passive drips',
        'Out of views']

#  Loops through all of the files in the current navigated directory
for file in os.listdir('.'):
    # initializing the titles and rows list for current file
    rows = []

    # reading csv file
    with open(file, 'r') as csvfile:
        #   The following if statement ignores the final file in case the
        #   script is ran more than once
        if(str(file) != "final_csv_data.csv"):
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # Initialize list that will contain each cell's value information
            numbers = []

            # Gets the different value cells depending on their
            # location. First is row number and second is column numbers
            # field_containing_all_rows[row_number][column_number]
            ratid = rows[1][6]
            title = rows[2][6]
            response_time = rows[3][6]
            scorer = rows[4][6]
            locomotion = rows[5][6]
            out_view_time = rows[20][6]

            # Adds all values onto the row to be added for this file
            # 'extend' instead of 'append' allows you to add more than one
            # argument onto the list.
            numbers.extend((ratid, title, response_time, scorer, locomotion, out_view_time))

            # Loops through from row 8 and on to get the value cells
            for row in rows[8:]:
                # Gets the value in column 9 for each row and appends (transposed)
                numbers.append(row[9])

            # At then end of each file the list 'numbers' represents the row containing
            # all of the values for this file, it's added to 'all_rows' because
            # all_rows will later be written onto the final csv file
            all_rows.append(numbers)

    # End of for loop, all values have been extracted from each file and are
    # all now located in 'all_rows'

# Name of csv file
filename = "final_csv_data.csv"
# Writing to csv file ('w+' mode clears the file before writing to it)
with open(filename, 'w+') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the title fields
    csvwriter.writerow(fields)
    # writing all of the rows containing the values
    csvwriter.writerows(all_rows)
