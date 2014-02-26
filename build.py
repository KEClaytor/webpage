# Simple website builder.
# Requires a source/ folder with two files:
#  __template__.html
#     This is the template HTML file which contains 
#     keywords that will be replaced:
#       <!--NAVIGATION--!>
#       <!--CONTENT--!>

import os

# Load up the template, search for the keywords and do the replacements
def fill_template(content_file):
    template = open('source/__template__.html')
    extra = open('source/__extra__.html')
    navbar = open('source/__navbar__.html')
    split_content_file = content_file.split('-')
    content = open('source/'+content_file)
    out = open(split_content_file[-1],'w')
    for template_line in template:
        if '<!--CONTENT--!>' in template_line:
            for content_line in content:
                out.write(content_line)
        elif '<!--EXTRA--!>' in template_line:
            for extra_line in extra:
                out.write(extra_line)
        elif '<!--BANNER--!>' in template_line:
            make_banner(out, split_content_file[-1])
        elif '<!--NAVBAR--!>' in template_line:
            for navbar_line in navbar:
                out.write(navbar_line)
        else:
            out.write(template_line)

# Title our page based on the content
def make_banner(out, title_string):
    sub_title = title_string.split('.')
    banner_string = '<h2>Kevin Claytor: %s</h2>\n' % (sub_title[0])
    out.write(banner_string)

# Later generate the navbar programatically
def make_navbar(out, content_file):
    pass

def build():
    # Load the source file

    # Loop over all the files 
    files = os.listdir("source/")
    for source_file in files:
        # Ignore our __NN__.html files
        if '__.html' not in source_file:
            fill_template(source_file)

if __name__ == '__main__':
    build()
