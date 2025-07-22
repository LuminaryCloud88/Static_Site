from textnode import TextType,TextNode



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