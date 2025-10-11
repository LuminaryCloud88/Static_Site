from enum import Enum
from split_blocks import markdown_to_blocks
import re 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.splitlines()
    stripped_lines = [line.strip() for line in lines if line.strip()]

    # Heading
    if stripped_lines and re.match(r"^#{1,6} ", stripped_lines[0]):
        return BlockType.HEADING

    # Code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Quote (allow '>' or '> ' and ignore empties)
    lstripped = [l.lstrip() for l in block.splitlines() if l.strip()]
    if lstripped and all(l.startswith(">") for l in lstripped):
        return BlockType.QUOTE

    # Unordered list
    if stripped_lines and all(line.startswith("- ") for line in stripped_lines):
        return BlockType.UNORDERED_LIST

    # Ordered list
    if stripped_lines and all(re.match(rf"^{i+1}\. ", line) for i, line in enumerate(stripped_lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH