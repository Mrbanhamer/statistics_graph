from graphs.graphs import graph
from requests.api_connector import connecting

# Separate the fetching from the graphing
sek, usd, gbp = connecting()

# Now pass all three to the graph function
graph(sek, usd, gbp)