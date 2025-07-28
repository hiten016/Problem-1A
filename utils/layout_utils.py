 def is_centered(x0, page_width):
    center = page_width / 2
    return abs(x0 - center) < page_width * 0.1

def is_heading_like(text):
    return text.isupper() or text.endswith(':') or text[0].isdigit()
