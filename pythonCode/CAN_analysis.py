# The CAN data is saved to a file in ASCII format
# An example of data would be
#       409.061036 1 99 Tx d 8 05 00 0C 29 00 C8 00 1A
#       
#       409.061036 ------------------> timestamp
#       1          ------------------> CAN channel 
#       99         ------------------> CAN ID in hex (0x99 is the TPM_MESS1 message)
#       "d 8"      ------------------> Dynamic length of the data in bytes, it is pretty
#                                      much 8 bytes 100% of the time
#       05 00 0C 29 00 C8 00 1A -----> The poyload I need to parse
#       05 (from above) -------------> This is the first vyte which indicates
#                                      the multiplexer byte. Look at the DBC,
#                                      check what information is provided in
#                                      multiplexer page 0x05 and use it if
#                                      it is useful 

import pandas as pd

can_data = []
example_str = []
temp = []
temp1 = []

df = pd.read_csv("E-Class_80KPH_A6_245.asc")
example_str = df.loc[595]                               # Puts the data at line 595 into example_str

temp = example_str.replace(' ','',regex=True)           # This removes the white space
temp1 = pd.Series.to_string(temp)                       # Converts to a string
str_length = len(temp1)                                 # String length
