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

def genhtml(para): # Function to write the HTML content to the index.html file
    with open('Rename/index.html', 'a') as f:
        f.write(para)
        f.write('\n')  # Add a newline after each line
if os.path.exists('Rename/index.html'):
    print("index.html already exists.") # Check if index.html already exists
else:
    with open('other/test.txt', 'r', encoding='utf-8') as pl:
        for line in pl:
            if 'marker' in line:  # Replace with your condition
                break
            html1 = line.strip() # first part of html
            genhtml(html1)

    genhtml(titl) # Adding a the Title to the index.html file
                
    with open('other/test.txt', 'r', encoding='utf-8') as pl:
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
                genhtml(html2)
                #print(html2) # Test to see the conten

    genhtml(titl) # Adding a the Title to the index.html file
                
    with open('other/test.txt', 'r', encoding='utf-8') as pl:
        target_found = False
        for line in pl:
            if 'target3_marker' in line:
                target_found = True
                continue
            if target_found:
                html3 = line.strip() #third part of html
                genhtml(html3)
                #print(html3) # Test to see the content

    if os.path.exists('Rename/index.html'):
        print("index.html created successfully.") # Check if index.html was created successfully

# Try to see if can be optimized to read the file once and write to index.html in one go, instead of multiple reads and writes.

# 4) Create the BookReaderDemo.js file
