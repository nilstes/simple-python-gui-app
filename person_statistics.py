import matplotlib.pyplot as plt
import numpy as np

def show_bar_chart(counts, labels, ylabel, xlabel):
    x = np.arange(len(counts))
    plt.bar(x, height=counts)
    plt.xticks(x, labels)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    
def show_histogram(values, min, max, num_bins, ylabel, xlabel):
    bins = np.linspace(min, max, num_bins)
    plt.hist(values, bins)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    

# Test funksjon
#show_bar_chart([2, 16, 3, 1, 4.5], ["a", "b", "c", "d", "e"], "Antall", xlabel = "Kategori")
#show_histogram([10,41,72,45,51,52,51,54,56,81,43,42], 0, 100, 10, "Hei", "Hei")