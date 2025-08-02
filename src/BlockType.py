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

def block_to_block_type(cleaned_blocks):
    lines = cleaned_blocks.splitlines()

    if re.match(r"^#{1,6} ",lines[0]):
        return BlockType.HEADING
    if cleaned_blocks.startswith("```") and cleaned_blocks.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(re.match(rf"^{i+1}\. ", line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH