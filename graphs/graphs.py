import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats

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


def plot_averages(sek_data, usd_data, gbp_data):
    # 1. Extract just the rates from each list of dictionaries
    sek_rates = [item['rate'] for item in sek_data]
    usd_rates = [item['rate'] for item in usd_data]
    gbp_rates = [item['rate'] for item in gbp_data]

    # 2. Calculate the averages
    # Sum of rates divided by the number of entries
    averages = [
        sum(sek_rates) / len(sek_rates) if sek_rates else 0,
        sum(usd_rates) / len(usd_rates) if usd_rates else 0,
        sum(gbp_rates) / len(gbp_rates) if gbp_rates else 0
    ]

    labels = ['SEK', 'USD', 'GBP']
    colors = ['blue', 'green', 'red']

    # 3. Create the Bar Chart
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(labels, averages, color=colors, alpha=0.7)

    # 4. Add formatting
    ax.set_ylabel('Average Rate (vs 1 EUR)')
    ax.set_title('Average Exchange Rate (1993-2026)')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Add the exact average value on top of each bar for clarity
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.show()

def calculate_stats(sek_data, usd_data, gbp_data):
    def get_rates(data_list):
        return [entry['rate'] for entry in data_list]

    # Extract rates
    rates_dict = {
        "SEK": get_rates(sek_data),
        "USD": get_rates(usd_data),
        "GBP": get_rates(gbp_data)
    }

    results = {}
    
    # We compare each currency's mean to the value 1.0 (The Euro)
    for name, rates in rates_dict.items():
        # stats.ttest_1samp tests if the list mean is different from popmean (1.0)
        t_stat, p_val = stats.ttest_1samp(rates, popmean=1.0)
        results[name] = {"t": t_stat, "p": p_val, "mean": sum(rates)/len(rates)}

    # --- Visualization ---
    labels = list(results.keys())
    means = [results[l]["mean"] for l in labels]
    p_values = [results[l]["p"] for l in labels]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Graph 1: How far the average is from the Euro (1.0)
    ax1.bar(labels, means, color=['blue', 'green', 'red'], alpha=0.6)
    ax1.axhline(y=1.0, color='black', linestyle='--', label='Euro (Base 1.0)')
    ax1.set_title("Average Rate vs. Euro")
    ax1.set_ylabel("Value of 1 Euro")
    ax1.legend()

    # Graph 2: The P-Value (Is the distance "Real"?)
    # We use a threshold of 0.05. If the bar is BELOW the line, it's significant.
    ax2.bar(labels, p_values, color='purple')
    ax2.axhline(y=0.05, color='red', linestyle='--', label='Significance (0.05)')
    ax2.set_yscale('log') # Log scale helps see very small p-values
    ax2.set_title("Statistical Significance (P-Value)")
    ax2.set_ylabel("Probability (P)")
    ax2.legend()

    plt.tight_layout()
    plt.show()

    # Print results for your presentation notes
    for name, data in results.items():
        status = "Significantly Different" if data["p"] < 0.05 else "Not Significantly Different"
        print(f"{name}: Mean={data['mean']:.2f}, P-Value={data['p']:.4e} ({status})")
# Usage:
# sek, usd, gbp = connecting()
# plot_averages(sek, usd, gbp)

# To run it, use the data from your connecting() function:
# sek, usd, gbp = connecting()
# graph(sek, usd, gbp)