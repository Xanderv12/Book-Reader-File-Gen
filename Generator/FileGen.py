import configparser
import os

# Config path Creation
configFolder = 'config'
configFile = 'config.ini'
configPath = os.path.join(configFolder, configFile)

config = configparser.ConfigParser()
config.read(configPath)

# Gather variables for each configuration value from config.ini

#Directories Varibles
baseDir = config['DIRECTORIES']['BaseDirectory']
secondDir = config['DIRECTORIES']['SecondDirectory']
contentDir = config['DIRECTORIES']['ContentDirectory']
urlPath = f'https://archives.library.wcsu.edu/{baseDir}/{secondDir}/{contentDir}/' # URL path for the archives library


# Data Variables
titl = config['INFORMATION']['Title']
pNum = int(config['INFORMATION']['Pages'])
h = int(config['INFORMATION']['Height'])
w = int(config['INFORMATION']['Width'])
bName = config['INFORMATION']['Base']



# 1) Create Directory where all files will be stored
try:
    os.makedirs(f'{contentDir}')
    print("Directory created successfully.")
except FileExistsError:
    print("Directory already exists.")



# 2) Creates BookReaderDemo.css file

# CSS file path and content
cssName = 'BookReaderDemo.css' # Name of the CSS file
cssPath = os.path.join(contentDir, cssName)

lines = [
    "/*Custom overrides for BookReader Demo.*/\n\n", 
    "/* Hide print and embed functionality */\n", 
    "#BRtoolbar .embed, .print {\n", 
    "display: none;\n", 
    "}"
]

try:
    with open(cssPath, "x") as pl:
        pl.writelines(lines)
    print("BookReaderDemo.css created successfully.") # File creation confirmed
except FileExistsError:
    print("BookReaderDemo.css already exists.")

# Folder and Files Names that contains the template files of the HTML and JavaScript content
tempFolder = 'templates'
htmlName = 'html.txt'
jsName = 'Javascript.txt'
htmlTempPath = os.path.join(tempFolder, htmlName)
jsTempPath = os.path.join(tempFolder, jsName)


# 3) Read contents of text file that holds the HTML
indexName = 'index.html'
indexPath = os.path.join(contentDir, indexName) # index.html file that will be written to

def genhtml(para): # Function to write the HTML content to the index.html file
    with open(indexPath, 'a') as f:
        f.write(para)
        f.write('\n')  # Add a newline after each line

if os.path.exists(indexPath):
    print("index.html already exists.") # Check if index.html already exists
else:
    with open(htmlTempPath, 'r', encoding='utf-8') as pl:
        for line in pl:
            if 'marker' in line:  # Replace with your condition
                break
            html1 = line.strip() # first part of html
            genhtml(html1)

    genhtml(titl) # Adding a the Title to the index.html file
                
    with open(htmlTempPath, 'r', encoding='utf-8') as pl:
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
                #print(html2) # Test to see the content

    genhtml(titl) # Adding a the Title to the index.html file
                
    with open(htmlTempPath, 'r', encoding='utf-8') as pl:
        target_found = False
        for line in pl:
            if 'target3_marker' in line:
                target_found = True
                continue
            if target_found:
                html3 = line.strip() #third part of html
                genhtml(html3)
                #print(html3) # Test to see the content

    print("index.html created successfully.") # Check if index.html was created successfully

# Try to see if can be optimized to read the file once and write to index.html in one go, instead of multiple reads and writes.



# 4) Create the BookReaderJSSimple.js file
jsBookName = 'BookReaderJSSimple.js'
jsBookPath = os.path.join(contentDir, jsBookName) # BookReaderJSSimple.js file that will be written to

def genjs(para): # Function to write the JavaScript content to the BookReaderJSSimple.js file
    with open(jsBookPath, 'a') as f:
        f.write(para)
        f.write('\n')  # Add a newline after each line

if os.path.exists(jsBookPath):
    print("BookReaderJSSimple.js already exists.")
else:
    with open(jsTempPath, 'r', encoding='utf-8') as rf:
        for line in rf:
            if 'firstMarker' in line:
                break
            js_content1 = line.strip() # first part of JavaScript content
            genjs(js_content1)

    genjs(f'return {w}; //Dynamically Added') #Adding with width return line

    with open(jsTempPath, 'r', encoding='utf-8') as rf:
        in_section = False
        for line in rf:
            if 'secondMarker' in line:
                in_section = True
                continue
            if 'thirdMarker' in line:
                in_section = False
                break
            if in_section:
                js_content2 = line.strip() # second part of JavaScript content
                genjs(js_content2)

    genjs(f'return {h}; //Dynamically Added') #Adding with height return line

    with open(jsTempPath, 'r', encoding='utf-8') as rf:
        in_section = False
        for line in rf:
            if 'fourthMarker' in line:
                in_section = True
                continue
            if 'fifthMarker' in line:
                in_section = False
                break
            if in_section:
                js_content3 = line.strip() # third part of JavaScript content
                genjs(js_content3)

    genjs(f'var leafStr = \'{bName}\'; //Dynamically Added')

    with open(jsTempPath, 'r', encoding='utf-8') as rf:
        in_section = False
        for line in rf:
            if 'sixthMarker' in line:
                in_section = True
                continue
            if 'seventhMarker' in line:
                in_section = False
                break
            if in_section:
                js_content4 = line.strip() # fourth part of JavaScript content
                genjs(js_content4)

    genjs(f'var url = \'{urlPath}\' + leafStr.replace(re, imgStr) + \'.jpg\'; //Dynamically Added') #Adding with URL path return line

    with open(jsTempPath, 'r', encoding='utf-8') as rf:
        in_section = False
        for line in rf:
            if 'eighthMarker' in line:
                in_section = True
                continue
            if 'ninthMarker' in line:
                in_section = False
                break
            if in_section:
                js_content5 = line.strip() # fifth part of JavaScript content
                genjs(js_content5)

    genjs(f'br.numLeafs = {pNum}; //Dynamically Added')

    with open(jsTempPath, 'r', encoding='utf-8') as rf:
        in_section = False
        for line in rf:
            if 'tenthMarker' in line:
                in_section = True
                continue
            if 'eleventhMarker' in line:
                in_section = False
                break
            if in_section:
                js_content6 = line.strip() # sixth part of JavaScript content
                genjs(js_content6)

    genjs(f'br.bookTitle= \'{titl}\'; //Dynamically Added')

    with open(jsTempPath, 'r', encoding='utf-8') as rf:
        in_section = False
        for line in rf:
            if 'twelfthMarker' in line:
                in_section = True
                continue
            if in_section:
                js_content7 = line.strip() # seventh part of JavaScript content
                genjs(js_content7)
    print("BookReaderJSSimple.js created successfully.")
