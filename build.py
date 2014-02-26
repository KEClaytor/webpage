# Simple website builder.
# Requires a source/ folder with two files:
#  __template__.html
#     This is the template HTML file which contains 
#     keywords that will be replaced:
#       <!--NAVIGATION--!>
#       <!--CONTENT--!>

import os

def fill_template(content_file):
    template = open('source/__template__.html')
    content = open('source/'+content_file)
    out = open(content_file,'w')
    for template_line in template:
        if '<!--CONTENT--!>' in template_line:
            for content_line in content:
                out.write(content_line)
        else:
            out.write(template_line)

def build():
    # Load the source file

    # Loop over all the files 
    files = os.listdir("source/")
    for source_file in files:
        if '__.html' not in source_file:
            fill_template(source_file)

if __name__ == '__main__':
    build()
