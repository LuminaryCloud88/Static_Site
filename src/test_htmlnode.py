import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="img", props={"src": "image.png", "alt": "Description"})
        html = node.props_to_html()
        self.assertIn('src="image.png"', html)
        self.assertIn('alt="Description"', html)
        self.assertEqual(html.count("="), 2)

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="Some text")
        self.assertEqual(node.props_to_html(), "")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Important", {"class": "highlight", "id": "main-text"})
        html = node.to_html()
        self.assertTrue(html.startswith("<span"))
        self.assertIn('class="highlight"', html)
        self.assertIn('id="main-text"', html)
        self.assertTrue(html.endswith("Important</span>"))

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_multiple_children(self):
        child1 = LeafNode("p", "First")
        child2 = LeafNode("p", "Second")
        parent = ParentNode("section", [child1, child2])
        self.assertEqual(parent.to_html(), "<section><p>First</p><p>Second</p></section>")

    def test_to_html_nested_with_attributes(self):
        child = LeafNode("a", "Link", {"href": "https://example.com"})
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><a href="https://example.com">Link</a></div>')

    def test_to_html_deeply_nested(self):
        node = ParentNode("html", [
            ParentNode("body", [
                ParentNode("div", [
                    LeafNode("p", "Deep content")
                ])
            ])
        ])
        self.assertEqual(node.to_html(), "<html><body><div><p>Deep content</p></div></body></html>")



if __name__ == "__main__":
    unittest.main()