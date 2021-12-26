# I'm trying to copy the files from one folder, into another, and renamed them

import shutil,os, glob                                                          # Imports required modules

reworked_filename_list = []                                                     # Sets up empty list for renaming

### Changes directory to...
os.chdir('C:/Users/a1038064/Documents/GitHub/pythonCode/batch_renaming/original_data')
dir_len = len(os.listdir())                                                     # Gets length of directory
# file_list = os.listdir('C:/Users/a1038064/Desktop/Current/RearrangingSharePointData/Data_Original')
# print(dir_len)

file_list = glob.glob('*.csv')                                                  # Gets a list of *.csv files only, and passes it to file_list

# Function below is stripping off some sections of the filename which we don't need
for file in file_list:
    filename = file
    reworked_filename = filename[0:-4]                                         # This gets me part of the filename I want (in this example, just 'ROAD_DATA_ORK_180KPH_E-CLASS')
    reworked_filename_list.append(reworked_filename)                            # Appends to a new list


file_extension = ".csv"                                                         # File extension string used to rebuild filenames
x = 1                                                                           # Used for moving through the files in the folder
# zeros = []                                                                      # Generates empty array to store zeros
# Function to rebuild the filenames below
for reworked_filename in reworked_filename_list:                                # Loop to move through files in reworked_filename_list
#    if x <= 10:
#        zeros = "00000"
#    elif x > 10:
#        zeros = "0000"
    num = reworked_filename[-6:]                                                # Gets the full number from the end of the original file name format (ie. 000113)
    num = num[-4:]                                                              # Only want 4 leading digits
    filename_main_body = reworked_filename[0:-7]

    original_file_name = file_list[x-1]                                         # [x - 1] because we index from zero
    # dest_file_name = reworked_filename + zeros + str(x) + file_extension        # New filename
    dest_file_name = num + "_" + filename_main_body + file_extension
    
    # dest_file_name = dest_file_name.strip("0")

    shutil.move("C:/Users/a1038064/Documents/GitHub/pythonCode/batch_renaming/original_data/" + original_file_name,
            "C:/Users/a1038064/Documents/GitHub/pythonCode/batch_renaming/Data_NewFormat/" + dest_file_name)

    x = x + 1                                                                   # Increment to move to next file
