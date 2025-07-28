import matplotlib.pyplot as plt

def plot_elements(elements):
    for el in elements:
        plt.text(el['x0'], el['y0'], el['text'], fontsize=el['font_size'])
    plt.gca().invert_yaxis()
    plt.show()
