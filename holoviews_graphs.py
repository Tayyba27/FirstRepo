import numpy as np
import holoviews_graphs as hv
from holoviews_graphs import dim, opts

hv.extension('bokeh', 'matplotlib')

dataset = [
        ('Resident Evil 2002', 6.7),
        ('Resident Evil: Apocalypse 2004',6.2 ),
        ('Resident Evil: Extinction 2007', 6.3),
        ('Resident Evil: Afterlife 2010', 5.8),
        ('Resident Evil: Retribution 2012', 5.4),
        ('Resident Evil: The Final Chapter', 5.5)
]
dataset

scatter_plot = hv.Points(dataset, label= 'Resident Evil Franchies IMDB')
scatter_plot
from holoviews_graphs import opts
scatter_plot.opts(
     xlabel = 'IMDB Rating',
     ylabel = 'Movie Title',
       size = 10,
     color  = 'coral',
     width  = 300,
    height  = 300
)




















