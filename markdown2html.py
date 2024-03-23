#!/usr/bin/python3
"""
Creating a program that converts Markdown files to html files
"""
import sys
import os

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    sys.stderr.write(f"Missing {input_file}\n")
    sys.exit(1)

sys.exit(0)

# if __name__ == "__main__":