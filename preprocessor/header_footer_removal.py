def remove_headers_footers(elements, height_threshold):
    return [el for el in elements if el['y0'] > height_threshold] 
