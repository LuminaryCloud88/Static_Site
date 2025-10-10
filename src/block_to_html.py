from split_blocks import markdown_to_blocks
from BlockType import *
from htmlnode import *
from text_to_textnode import text_to_textnode
from textnode import *
from converter import *

def text_to_children(text):
    text_nodes = text_to_textnode(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    print("DEBUG - Blocks:")
    for i, block in enumerate(blocks):
        print(f"Block {i}: {repr(block)}")
        print(f"Type: {block_to_block_type(block)}")
    print("---")
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            lines = block.splitlines()
            
            for line in lines:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                    
                # Count the # characters
                level = 0
                for char in stripped_line:
                    if char == "#":
                        level += 1
                    else:
                        break
                
                # Extract text after the #'s and the space
                text = stripped_line[level:].strip()
                children = text_to_children(text)
                node = ParentNode(tag=f"h{level}", children=children)
                block_nodes.append(node)
            
            continue  # Skip the normal append since we already added nodes
        
        elif block_type == BlockType.PARAGRAPH:
            import re
            cleaned_text = re.sub(r'\s+', ' ', block).strip()
            children = text_to_children(cleaned_text)
            node = ParentNode(tag="p", children=children)
        
        elif block_type == BlockType.CODE:
            lines = block.splitlines()
            code_lines = [line.strip() for line in lines[1:-1]]
            code_content = "\n".join(code_lines) + "\n"  # Add trailing newline
            text_node = TextNode(code_content, TextType.TEXT)
            code_child = text_node_to_html_node(text_node)
            node = ParentNode(tag="pre", children=[ParentNode(tag="code", children=[code_child])])
        
        elif block_type == BlockType.QUOTE:
            lines = block.splitlines()
            cleaned_lines = []
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("> "):
                    cleaned_lines.append(stripped[2:])
                elif stripped.startswith(">"):
                    cleaned_lines.append(stripped[1:])
            cleaned_text = " ".join(cleaned_lines)
            children = text_to_children(cleaned_text)
            node = ParentNode(tag="blockquote", children=children)

        elif block_type == BlockType.UNORDERED_LIST:
            items = block.splitlines()
            list_items = []
            for item in items:
                content = item.strip()[2:]  # remove "- "
                children = text_to_children(content)
                list_items.append(ParentNode(tag="li", children=children))
            node = ParentNode(tag="ul", children=list_items)

        elif block_type == BlockType.ORDERED_LIST:
            items = block.splitlines()
            list_items = []
            for item in items:
                content = item.strip().split(".", 1)[1].strip() if "." in item else item
                children = text_to_children(content)
                list_items.append(ParentNode(tag="li", children=children))
            node = ParentNode(tag="ol", children=list_items)

        else:
            children = text_to_children(block)
            node = ParentNode(tag="p", children=children)

        block_nodes.append(node)

    return ParentNode(tag="div", children=block_nodes)