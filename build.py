# Simple website builder.
# Requires a source/ folder with two files:
#  __template__.html
#     This is the template HTML file which contains 
#     keywords that will be replaced:
#       <!--NAVIGATION--!>
#       <!--CONTENT--!>

import os

# Load up the template, search for the keywords and do the replacements
def fill_template(sourcefile):
    # Open our templates and other source files
    content = open(sourcefile)
    directory = '/'.join(x for x in sourcefile.split('/')[0:-1])
    content_file = sourcefile.split('/')[-1]
    filename = content_file.split('.')[0]
    # These are always in the source
    template = open('source/__template__.html')
    contact = open('source/__contact__.html')
    analytics = open('source/__analytics__.html')
    # There may be another navbar in a sub-folder, try to use it
    try:
        navbar = open('/'.join(x for x in [directory, '__navbar__.html']))
    except:
        print 'could not find __navbar__.html in ' + directory
        print 'opening default navbar'
        navbar = open('source/__navbar__.html')

    # Open the file we are writing to
    out = open(os.path.join('out',content_file),'w')
    for template_line in template:
        if '<!--ANALYTICS--!>' in template_line:
            for analytics_line in analytics:
                out.write(analytics_line)
        elif '<!--CONTENT--!>' in template_line:
            for content_line in content:
                out.write(content_line)
        elif '<!--CONTACT--!>' in template_line:
            for contact_line in contact:
                out.write(contact_line)
        elif '<!--BANNER--!>' in template_line:
            make_banner(out, filename)
        elif '<!--NAVBAR--!>' in template_line:
            for navbar_line in navbar:
                out.write(navbar_line)
        else:
            out.write(template_line)

# Title our page based on the content
def make_banner(out, title_string):
    sub_title = title_string.split('.')
    if sub_title[0] == 'index':
        sub_title[0] = 'home'
    banner_string = '<h1 class="in-page-title">Kevin Claytor: %s</h1>\n' % (sub_title[0])
    banner_string = '<h1 class="in-page-title-basic">Kevin Claytor</h1>\n'
    out.write(banner_string)

# Later generate the navbar programatically
def make_navbar(out, content_file):
    pass

def build():
    # Load the source file

    ## Loop over all the files 
    #files = os.listdir("source/")
    #for source_file in files:
    #    # Ignore our __NN__.html files
    #    if '__.html' not in source_file:
    #        fill_template(source_file)

    # Recursively loop through the files and build the .html ones
    for dirname, dirnames, filenames in os.walk('./source/'):
        for filename in filenames:
            sourcefile = os.path.join(dirname, filename)
            if '.html' in sourcefile and '__.html' not in sourcefile:
                fill_template(sourcefile)

if __name__ == '__main__':
    build()
