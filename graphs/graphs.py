import matplotlib.pyplot as plt
from datetime import datetime

def graph(sek_data, usd_data, gbp_data):
    # Helper function to extract dates and rates from the list of dicts
    def process_data(data_list):
        dates = []
        rates = []
        for entry in data_list:
            # Note: Frankfurter API usually uses YYYY-MM-DD
            # If your dates are DD-MM-YYYY, keep your current format
            clean_date = datetime.strptime(entry['date'], "%Y-%m-%d")
            dates.append(clean_date)
            rates.append(entry['rate'])
        return dates, rates

    # Extract data for all three
    sek_dates, sek_rates = process_data(sek_data)
    usd_dates, usd_rates = process_data(usd_data)
    gbp_dates, gbp_rates = process_data(gbp_data)

    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot each line with a different color and label
    ax.plot(sek_dates, sek_rates, label='SEK (Swedish Krona)', color='blue', linewidth=2)
    ax.plot(usd_dates, usd_rates, label='USD (US Dollar)', color='green', linewidth=2)
    ax.plot(gbp_dates, gbp_rates, label='GBP (British Pound)', color='red', linewidth=2)

    # Formatting the chart
    ax.set(xlabel='Date', 
           ylabel='Rate (Relative to 1 EUR)',
           title='European Currency Exchange Rates Over Time')
    
    ax.grid(True, linestyle='--', alpha=0.6)
    fig.autofmt_xdate() # Prevents date overlap
    
    # Add a legend so we know which color is which
    ax.legend()

    plt.tight_layout()
    plt.show()

# To run it, use the data from your connecting() function:
# sek, usd, gbp = connecting()
# graph(sek, usd, gbp)