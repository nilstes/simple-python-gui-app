import matplotlib.pyplot as plt
import numpy as np

def show_histogram(counts, labels, ylabel, xlabel):
    x = np.arange(len(counts))
    plt.bar(x, height=counts)
    plt.xticks(x, labels)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    
# Test funksjon
#show_histogram([2, 16, 3, 1, 4.5], ["a", "b", "c", "d", "e"], "Antall", xlabel = "Kategori")