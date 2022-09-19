import os
from bs4 import BeautifulSoup
import pandas as pd  

d = {"Genome Name": [],
    "Coarse consistency (%)": [],
    "Fine consistency (%)": [],
    "Completeness (%)": [],
    "Contamination (%)": []}

  
def get_data_from_html(fname):

    # Opening the html file. If the file
    # is present in different location, 
    # exact location need to be mentioned
    HTMLFileToBeOpened = open(fname, "r")
    # Reading the file and storing in a variable
    contents = HTMLFileToBeOpened.read()
    
    # Creating a BeautifulSoup object and
    # specifying the parser 
    beautifulSoupText = BeautifulSoup(contents, 'lxml')

    # Using the prettify method to modify the code
    #  Prettify() function in BeautifulSoup helps
    # to view about the tag nature and their nesting
    print_next = False
    must_find = ["Coarse consistency (%)","Fine consistency (%)", "Completeness (%)","Contamination (%)","Genome Name"]
    def must_print(string):
        if(string in must_find):
            return string
        else: 
            return False


    for row in beautifulSoupText.find_all('tr'):
        for child in row.contents:
                try:
                    if(print_next != False):
                        if(print_next == "Genome Name"):
                             d[print_next].append(child.contents[0].split(" Annotation")[0])
                        else: d[print_next].append(child.contents[0])
                        print_next = False
                    if(must_print(child.contents[0]) != False):
                        print_next = child.contents[0]
                except:
                    None

# Get current working directory
directory = os.getcwd()
for filename in os.listdir(directory):
      
    # check whether the file is having
    # the extension as html and it can
    # be done with endswith function
    if filename.endswith('.html'):
          
        # os.path.join() method in Python join
        # one or more path components which helps
        # to exactly get the file
        fname = os.path.join(directory, filename)
        get_data_from_html(fname)

df = pd.DataFrame(data=d)  
df.to_csv('patric_quality_summary.tsv', sep='\t', encoding='utf-8', index=False)
