import unittest
from textnode import TextNode, TextType
from split_delimiter import *
from text_to_textnode import text_to_textnode

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnodes_full_markdown(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )

        result = text_to_textnode(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(result, expected)

    def test_text_to_textnodes_plain_text(self):
        text = "This is just plain text without any formatting."

        result = text_to_textnode(text)

        expected = [TextNode("This is just plain text without any formatting.", TextType.TEXT)]

        self.assertListEqual(result, expected)

    def test_text_to_textnodes_bold_only(self):
        text = "This is **bold** text."

        result = text_to_textnode(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]

        self.assertListEqual(result, expected)

    def test_text_to_textnodes_unmatched_bold_delimiter(self):
        text = "This is **bold text without a closing delimiter"

        with self.assertRaises(ValueError):
            text_to_textnode(text)

    def test_text_to_textnodes_image_only(self):
        text = "![alt](https://example.com/img.png)"

        result = text_to_textnode(text)

        expected = [
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png")
        ]

        self.assertListEqual(result, expected)

    def test_text_to_textnodes_multiple_formats_inline(self):
        text = "**bold**_italic_`code`"

        result = text_to_textnode(text)

        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code", TextType.CODE),
        ]

        self.assertListEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()