import matplotlib.pyplot as plot
import numpy

def sort_labels(label_data_map, sorted_data):
    sorted_labels = []
    labels = label_data_map.keys()
    
    for i in sorted_data:
        for label in labels:
            if label_data_map[label] == i and label not in sorted_labels:
                sorted_labels.append(label)
    return sorted_labels
    
def normalize_plot(label_data_map, filename):
    plot.rcdefaults()
    
    fig, axes = plot.subplots()

    data = sorted(list(label_data_map.values()))
    labels = sort_labels(label_data_map, data)
    
    x_pos = numpy.arange(len(labels))
    
    bars = axes.bar(x_pos, data)
    axes.set_xticks(x_pos)
    axes.set_xticklabels(labels)
    axes.axhline(numpy.mean(data), color='orange', linewidth=2)
    
    font_size = 10
    
    if len(data) > 9:
        font_size = 7
        
    axes.bar_label(bars, labels=['{:,.1%}'.format(i) for i in numpy.true_divide(data,sum(data))], size=font_size, weight='bold')
    axes.set_ylabel('Count')
    axes.set_title('Jûngle Type Stats')
    
    fig.savefig(f'{filename}.png')