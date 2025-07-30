import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter,split_nodes_image,split_nodes_link

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

    def test_split_images(self):
        node = TextNode(
         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_nodes_image_with_multiple_images(self):
        node = TextNode(
            "Intro text ![first](http://img1.png) middle ![second](http://img2.png) end",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Intro text ", TextType.TEXT),
                TextNode("first", TextType.IMAGE, "http://img1.png"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("second", TextType.IMAGE, "http://img2.png"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image_with_no_images(self):
        node = TextNode("Just plain text.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("Just plain text.", TextType.TEXT)],
            new_nodes,
        )

    def test_split_nodes_image_with_non_text_node(self):
        node = TextNode("![alt](url)", TextType.IMAGE, "url")
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_nodes_link_with_multiple_links(self):
        node = TextNode(
            "Check this [link1](http://a.com) and [link2](http://b.com) now",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Check this ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "http://a.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "http://b.com"),
                TextNode(" now", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_link_with_no_links(self):
        node = TextNode("No markdown links here.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("No markdown links here.", TextType.TEXT)],
            new_nodes,
        )

    def test_split_nodes_link_with_non_text_node(self):
        node = TextNode("link", TextType.LINK, "http://example.com")
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

if __name__ == "__main__":
    unittest.main()


