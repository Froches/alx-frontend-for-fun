#!/usr/bin/python3
"""
Creating a program that converts Markdown files to html files
"""


import sys
import os
import markdown


def parse_markdown_headings(markdown_text):
    """
    Parses markdown headings
    """
    html_content = ""
    new_lines = markdown_text.split("\n")
    for line in new_lines:
        if line.startswith("#"):
            h_level = line.count("#")
            title = line.strip("#").strip()
            html_content += f"<h{h_level}>{title}</h{h_level}>\n"
        else:
            html_content += f"{line}\n"
    return html_content


def convert_markdown_to_html(input_file, output_file):
    """
    Does the conversion
    """
    try:
        with open(input_file, 'r') as md_file:
            markdown_text = md_file.read()
            html_content = markdown.markdown(markdown_text)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
