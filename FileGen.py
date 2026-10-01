import configparser
import os

config = configparser.ConfigParser()
config.read('config/config.ini')

# Variables for each configuration value

#fol = config['INFORMATION']['Folder']
    # Possibly not needed

titl = config['INFORMATION']['Title']
pNum = int(config['INFORMATION']['Pages'])
h = int(config['INFORMATION']['Height'])
w = int(config['INFORMATION']['Width'])
bName = config['INFORMATION']['Base']


# 1) Create Directory where all files will be stored
try:
    os.makedirs('Rename')
    print("Directory created successfully.")
except FileExistsError:
    print("Directory already exists.")



# 2) Creates BookReaderDemo.css file
filename = 'BookReaderDemo.css' # Name of the CSS file
filepath = f'{'Rename'}/{filename}'

lines = [
    "/*Custom overrides for BookReader Demo.*/\n\n", 
    "/* Hide print and embed functionality */\n", 
    "#BRtoolbar .embed, .print {\n", 
    "display: none;\n", 
    "}"
]
try:
    with open(filepath, "x") as pl:
        pl.writelines(lines)
    print("BookReaderDemo.css created successfully.") # File creation confirmed
except FileExistsError:
    print("BookReaderDemo.css already exists.")
