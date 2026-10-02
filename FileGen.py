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

# 3) Read contents of text file that holds the HTML
with open('other/test.txt', 'r') as pl:
    for line in pl:
        if 'marker' in line:  # Replace with your condition
            break
        html1 = line.strip() #first part of html
        with open('Rename/index.html', 'a') as f:
            f.write(html1,{titl}) # Write the first part of the HTML with the inserted title


with open('other/test.txt', 'r') as pl:
    in_section = False
    for line in pl:
        if 'target1_marker' in line:
            in_section = True
            continue
        if 'target2_marker' in line:
            in_section = False
            break
        if in_section:
            html2 = line.strip() #second part of html
            #print(html2) # Test to see the conten
            
with open('other/test.txt', 'r') as pl:
    target_found = False
    for line in pl:
        if 'target3_marker' in line:
            target_found = True
            continue
        if target_found:
            html3 = line.strip() #third part of html
            #print(html3) # Test to see the content

