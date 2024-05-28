#!/usr/bin/python3
"""markdown2html.py - Converts a markdown file to HTML"""


import markdown
import sys


if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

try:
    with open(markdown_file, 'r') as file:
        text = file.read()
        html = markdown.markdown(text)
except FileNotFoundError:
    print("Missing {}".format(markdown_file))
    sys.exit(1)

with open(html_file, 'w') as file:
    file.write(html)
