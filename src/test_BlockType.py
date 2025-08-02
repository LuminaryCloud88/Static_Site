import unittest
from BlockType import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    # 1. Heading Tests
    def test_heading_single_hash(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)

    def test_heading_six_hashes(self):
        self.assertEqual(block_to_block_type("###### This is a heading"), BlockType.HEADING)

    def test_heading_too_many_hashes(self):
        self.assertEqual(block_to_block_type("#######Too many hashes"), BlockType.PARAGRAPH)

    def test_heading_missing_space(self):
        self.assertEqual(block_to_block_type("#No space after hash"), BlockType.PARAGRAPH)

    # 2. Code Block Tests
    def test_code_block_proper(self):
        self.assertEqual(block_to_block_type("```\nprint('hello')\n```"), BlockType.CODE)

    def test_code_block_missing_end(self):
        self.assertEqual(block_to_block_type("```\nprint('hello')"), BlockType.PARAGRAPH)

    def test_code_block_wrong_number_of_backticks(self):
        self.assertEqual(block_to_block_type("``\nprint('hello')\n``"), BlockType.PARAGRAPH)

    # 3. Quote Block Tests
    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_quote_multiline(self):
        self.assertEqual(block_to_block_type("> First line\n> Second line"), BlockType.QUOTE)

    def test_quote_partial_lines(self):
        self.assertEqual(block_to_block_type("> Good line\nMissing >"), BlockType.PARAGRAPH)

    # 4. Unordered List Tests
    def test_unordered_list_single(self):
        self.assertEqual(block_to_block_type("- Item one"), BlockType.UNORDERED_LIST)

    def test_unordered_list_multiple(self):
        self.assertEqual(block_to_block_type("- Item one\n- Item two"), BlockType.UNORDERED_LIST)

    def test_unordered_list_partial(self):
        self.assertEqual(block_to_block_type("- Item one\nNot a list"), BlockType.PARAGRAPH)

    # 5. Ordered List Tests
    def test_ordered_list_simple(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second"), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_start(self):
        self.assertEqual(block_to_block_type("2. Second\n3. Third"), BlockType.PARAGRAPH)

    def test_ordered_list_skipped_number(self):
        self.assertEqual(block_to_block_type("1. First\n3. Third"), BlockType.PARAGRAPH)

    # 6. Paragraph Tests
    def test_paragraph_normal(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph."), BlockType.PARAGRAPH)

    def test_paragraph_false_heading(self):
        self.assertEqual(block_to_block_type("#######No space"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
