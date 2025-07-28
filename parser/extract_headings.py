from parser.extract_features import group_text_blocks, merge_text_block

def is_heading(block, avg_font_size):
    text = block["text"]
    return (
        len(text.split()) <= 12 and
        text[-1] not in ['.', ':', ';'] and
        block["font_size"] >= avg_font_size + 1.0
    )

def extract_headings(layout_by_page):
    all_blocks = []
    for page in layout_by_page:
        grouped = group_text_blocks(page)
        merged = [merge_text_block(g) for g in grouped]
        all_blocks.extend(merged)

    font_sizes = [b["font_size"] for b in all_blocks]
    avg_font_size = sum(font_sizes) / len(font_sizes)

    headings = []
    for block in all_blocks:
        if is_heading(block, avg_font_size):
            level = assign_heading_level(block["font_size"], avg_font_size)
            headings.append({
                "level": level,
                "text": block["text"],
                "page": block["page_num"]
            })
    return headings

def assign_heading_level(font_size, avg_font_size):
    if font_size >= avg_font_size + 4:
        return "H1"
    elif font_size >= avg_font_size + 1.5:
        return "H2"
    else:
        return "H3"

