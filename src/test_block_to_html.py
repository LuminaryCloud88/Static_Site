import unittest
from block_to_html import *
from split_blocks import markdown_to_blocks
from BlockType import *
from htmlnode import *
from text_to_textnode import text_to_textnode
from textnode import *
from converter import *

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_heading(self):
        md = """
        # Heading Level 1
        ## Heading Level 2 with _italic_ text
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading Level 1</h1><h2>Heading Level 2 with <i>italic</i> text</h2></div>",
        )
    def test_blockquote(self):
        md = """
    > This is a quote with **bold** text
    > and it continues on a second line.
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>bold</b> text and it continues on a second line.</blockquote></div>",
        )
    def test_unordered_list(self):
        md = """
    - Item one with `code`
    - Item two with _italic_
    - Item three with **bold**
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one with <code>code</code></li><li>Item two with <i>italic</i></li><li>Item three with <b>bold</b></li></ul></div>",
        )
    def test_ordered_list(self):
        md = """
    1. First item
    2. Second item with **bold**
    3. Third item with _italic_ and `code`
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i> and <code>code</code></li></ol></div>",
        )
   
if __name__ == "__main__":
    unittest.main()