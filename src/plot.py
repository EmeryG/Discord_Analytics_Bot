import matplotlib.pyplot as plot
import numpy

def normalize_plot(label_data_map, filename):
    plot.rcdefaults()
    
    fig, axes = plot.subplots()
    
    labels = label_data_map.keys()
    data = label_data_map.values()
    
    y_pos = numpy.arange(len(labels))
    
    axes.barh(y_pos, data)
    axes.set_yticks(y_pos)
    axes.set_yticklabels(labels)
    axes.invert_yaxis()
    axes.set_xlabel('Count')
    axes.set_title('Jungle Type Stats')
    
    fig.savefig(f'{filename}.png')