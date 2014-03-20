webpage
=======

Python scripts and source* for generating my personal webpage.
Currently online at; http://people.duke.edu/~kec30/

Get up and running:
The script is a very simple grab and replace script. It looks for a __template__.html file in the source/ directory. Then fills that template using content files (*.html) and other code that you may want to be repeated (for example a navbar with __navbar__.html). You can use multiple __navbar__.html files by placing specific ones within sub-directories. This allows for you to make a branching layout.
The output files are dropped into the out/ directory. Note that this is a flat directory - all information regarding the build directory structure is lost. This allows for quick linking between files (you just have to remember the name), but take care not to use the same name twice.

*Currently does not include binaries, docs, or mfiles.
