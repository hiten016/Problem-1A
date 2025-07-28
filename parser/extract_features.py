from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

def extract_layout_by_page(pdf_path):
    layout_by_page = []
    for page_layout in extract_pages(pdf_path):
        page_elements = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    line_text = text_line.get_text().strip()
                    if not line_text:
                        continue
                    font_sizes = []
                    font_names = []
                    for char in text_line:
                        if isinstance(char, LTChar):
                            font_sizes.append(char.size)
                            font_names.append(char.fontname)
                    if font_sizes:
                        avg_font_size = sum(font_sizes) / len(font_sizes)
                        common_font = max(set(font_names), key=font_names.count)
                        page_elements.append({
                            "text": line_text,
                            "font_size": avg_font_size,
                            "font_name": common_font,
                            "x": text_line.bbox[0],
                            "y": text_line.bbox[1],
                            "page_num": page_layout.pageid
                        })
        layout_by_page.append(sorted(page_elements, key=lambda x: (-x["y"], x["x"])))
    return layout_by_page

def group_text_blocks(elements, y_thresh=5, font_thresh=1.5):
    grouped = []
    if not elements:
        return grouped
    current_block = [elements[0]]
    for i in range(1, len(elements)):
        prev = elements[i - 1]
        curr = elements[i]
        close_y = abs(prev["y"] - curr["y"]) <= y_thresh
        similar_font = abs(prev["font_size"] - curr["font_size"]) <= font_thresh
        if close_y and similar_font:
            current_block.append(curr)
        else:
            grouped.append(current_block)
            current_block = [curr]
    grouped.append(current_block)
    return grouped

def merge_text_block(block):
    return {
        "text": " ".join(line["text"] for line in block).strip(),
        "font_size": block[0]["font_size"],
        "font_name": block[0]["font_name"],
        "x": block[0]["x"],
        "y": block[0]["y"],
        "page_num": block[0]["page_num"]
    }
