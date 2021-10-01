# THIS IS ONLY A TEST TASK - DO NOT USE IT IN PRODUCTION!

Requirements:

0. Linux machine, of course..
1. Python 3 (tested on 3.6.8).
2. PyYAML: pip install --user pyyaml

Usage:

./fstab.py inputfile outputfile

Exit codes:

0 - if execution completed successfully;
1 - if we could not open input file;
2 - if we encounter problems with the output file;
3 - if PyYAML module is not available.
