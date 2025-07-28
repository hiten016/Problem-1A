'''import numpy as np
def generate_features(elements):
    features = []
    for el in elements:
        features.append([
            el['font_size'],
            1 if el['bold'] else 0,
            1 if el['text'].isupper() else 0,
            len(el['text']),
            sum(c.isdigit() for c in el['text'])
        ])
    return np.array(features)
'''
import numpy as np
import re
from collections import Counter

def generate_features_from_elements(elements):
    if not elements:
        return np.array([])
        
    font_sizes = [el['font_size'] for el in elements]
    body_font_size = Counter(font_sizes).most_common(1)[0][0] if font_sizes else 10.0

    features = []
    heading_pattern = re.compile(r'^\s*(\d+(\.\d+)*)\.?')

    for i, el in enumerate(elements):
        text = el['text']
        font_size = el['font_size']

        match = heading_pattern.match(text)
        if match:
            heading_depth = match.group(1).count('.') + 1
        else:
            heading_depth = 0
        
        prev_font_size = elements[i-1]['font_size'] if i > 0 else font_size
        font_increase_from_prev = 1 if font_size > prev_font_size else 0
        
        normalized_font_size = font_size / body_font_size

        features.append([
            normalized_font_size,
            1 if el['bold'] else 0,
            1 if text.isupper() else 0,
            len(text),
            heading_depth,
            font_increase_from_prev
        ])
        
    return np.array(features)

