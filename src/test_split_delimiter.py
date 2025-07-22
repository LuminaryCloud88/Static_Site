import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_backtick_delimiter(self):
        node = TextNode("This has `code` inside", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" inside", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_asterisk_delimiter_multiple(self):
        node = TextNode("This is **bold** and **strong** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("strong", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_underscore_delimiter_start_end(self):
        node = TextNode("_italic_ text and more _style_", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" text and more ", TextType.TEXT),
            TextNode("style", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("Some `broken code here", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_mixed_node_types(self):
        node1 = TextNode("**bold**", TextType.TEXT)
        node2 = TextNode("An image", TextType.IMAGE, url="img.png")
        result = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
            node2  
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()


