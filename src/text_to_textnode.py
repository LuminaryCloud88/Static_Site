from textnode import TextType,TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_delimiter import *

def text_to_textnode(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
     
    return nodes