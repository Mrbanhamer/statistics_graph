from graphs.graphs import graph, plot_averages
from api.api_connector import connecting

# Separate the fetching from the graphing
sek, usd, gbp = connecting()

# Now pass all three to the graph function
#graph(sek, usd, gbp)
plot_averages(sek, usd, gbp)