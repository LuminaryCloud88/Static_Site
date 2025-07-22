import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "Look at ![one](img1.png) and also ![two](img2.jpg)"
        )
        self.assertListEqual(
            [("one", "img1.png"), ("two", "img2.jpg")],
            matches
        )

    def test_extract_image_with_spaces_in_url(self):
        matches = extract_markdown_images(
            "Here is ![spacey](https://example.com/image%20file.png)"
        )
        self.assertListEqual(
            [("spacey", "https://example.com/image%20file.png")],
            matches
        )

    def test_extract_image_with_special_characters(self):
        matches = extract_markdown_images(
            "Icon: ![icon*](https://example.com/img?type=icon&version=1.0)"
        )
        self.assertListEqual(
            [("icon*", "https://example.com/img?type=icon&version=1.0")],
            matches
        )

    def test_extract_image_at_start(self):
        matches = extract_markdown_images(
            "![top](top.png) is the first thing."
        )
        self.assertListEqual([("top", "top.png")], matches)

    def test_no_images_returns_empty_list(self):
        matches = extract_markdown_images("This has no images at all.")
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()
