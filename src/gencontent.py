import os
from  block_to_html import markdown_to_html_node
from split_blocks import markdown_to_blocks

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    blocks = markdown_to_blocks(markdown_content)
    for i, b in enumerate(blocks):
        if b.lstrip().startswith(">"):
            print("QUOTE BLOCK:", repr(b))

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    print("<blockquote" in html, html.find("<blockquote"))

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as to_file:
        to_file.write(template)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")