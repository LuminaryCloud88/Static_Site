def markdown_to_blocks(markdown):
    blocks = []
    curr = []
    for line in markdown.splitlines():
        if line.strip() == "":
            if curr:
                blocks.append("\n".join(curr).strip())
                curr = []
        else:
            curr.append(line)
    if curr:
        blocks.append("\n".join(curr).strip())
    return blocks