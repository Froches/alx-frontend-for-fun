#!/usr/bin/python3
"""
markdown2html.py - Converts a markdown file to HTML

Usage:
    ./markdown2html.py README.md README.html

This script takes two arguments:
    1. The path to the input markdown file (e.g., README.md)
    2. The path to the output HTML file (e.g., README.html)

The script reads the content of the markdown file, converts it to HTML using
the `markdown` module, and writes the HTML content to the output file.

If the input markdown file does not exist, the script prints an error message
and exits with status code 1.
"""

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
