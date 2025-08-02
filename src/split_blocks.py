def markdown_to_blocks(markdown):

    raw_blocks = markdown.split("\n\n")

    cleaned_blocks = [block.strip() for block in raw_blocks if block.strip()]

    return cleaned_blocks