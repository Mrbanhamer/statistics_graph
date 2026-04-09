import matplotlib.pyplot as plt
from datetime import datetime

def sek(data):
    # We need to extract the rates and dates into two separate lists for plotting
    rates = []
    dates = []

    for entry in data:
        # entry is now {'rate': 11.20, 'date': '10-10-2025'}
        # We convert the date string to a real date object immediately
        clean_date = datetime.strptime(entry['date'], "%d-%m-%Y")
        
        # If you wanted to filter (e.g., only even rates), you do it here:
        if entry['rate'] % 2 == 0:
            # Maybe you only want even numbers? 
            # (Though in currency, rates are rarely whole even numbers!)
            pass 
        
        rates.append(entry['rate'])
        dates.append(clean_date)

    # Now we plot. Remember: (X-axis, Y-axis)
    # We put dates on X so the line moves from left to right over time.
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dates, rates, marker='o', color='green', label='SEK Rate')

    ax.set(xlabel='Date', 
           ylabel='Rate (SEK)',
           title='EUR to SEK conversion over time')
    
    ax.grid(True)
    fig.autofmt_xdate() # Keeps the dates from overlapping
    plt.legend()
    plt.show()

# Example of your new "Rate-First" data format:
history_data = [
    {'rate': 11.22, 'date': '10-10-2025'},
    {'rate': 11.45, 'date': '11-10-2025'},
    {'rate': 11.30, 'date': '12-10-2025'}
]

sek(history_data)

def pounds(data):
        # We need to extract the rates and dates into two separate lists for plotting
    rates = []
    dates = []

    for entry in data:
        # entry is now {'rate': 11.20, 'date': '10-10-2025'}
        # We convert the date string to a real date object immediately
        clean_date = datetime.strptime(entry['date'], "%d-%m-%Y")
        
        # If you wanted to filter (e.g., only even rates), you do it here:
        if entry['rate'] % 2 == 0:
            # Maybe you only want even numbers? 
            # (Though in currency, rates are rarely whole even numbers!)
            pass 
        
        rates.append(entry['rate'])
        dates.append(clean_date)

    # Now we plot. Remember: (X-axis, Y-axis)
    # We put dates on X so the line moves from left to right over time.
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dates, rates, marker='o', color='green', label='Pounds Rate')

    ax.set(xlabel='Date', 
           ylabel='Rate (Pounds)',
           title='EUR to Pounds conversion over time')
    
    ax.grid(True)
    fig.autofmt_xdate() # Keeps the dates from overlapping
    plt.legend()
    plt.show()