from textnode import TextType,TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
            else:
                for index, text in enumerate(parts):
                    if text == "":
                        continue
                    if index % 2 == 1:
                        special_text = TextNode(text, text_type, url=None)
                        new_nodes.append(special_text)
                    else:
                        regular_text = TextNode(text, TextType.TEXT, url=None)
                        new_nodes.append(regular_text) 
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            current_text = node.text
            if images == []:
                new_nodes.append(node)
            else:
                for alt_text, url in images:
                    image_markdown = f'![{alt_text}]({url})'
                    parts_before, parts_after = current_text.split(image_markdown, 1)
                    if parts_before != "":
                        text = TextNode(parts_before, TextType.TEXT, url=None)
                        new_nodes.append(text)
                    image = TextNode(alt_text, TextType.IMAGE, url)
                    new_nodes.append(image)
                    current_text = parts_after
                if current_text != "":
                    leftovers = TextNode(current_text, TextType.TEXT, url=None)
                    new_nodes.append(leftovers)
    return new_nodes
                




def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            current_text = node.text
            if links == []:
                new_nodes.append(node)
            else:
                for link_text, url in links:
                    link_markdown = f'[{link_text}]({url})'
                    parts_before, parts_after = current_text.split(link_markdown, 1)
                    if parts_before != "":
                        text = TextNode(parts_before, TextType.TEXT, url=None)
                        new_nodes.append(text)
                    link = TextNode(link_text, TextType.LINK, url)
                    new_nodes.append(link)
                    current_text = parts_after
                if current_text != "":
                    leftovers = TextNode(current_text, TextType.TEXT, url=None)
                    new_nodes.append(leftovers)
    return new_nodes