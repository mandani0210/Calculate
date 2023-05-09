import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)

    # Add line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = slope * x_pred + intercept
    ax.plot(x_pred, y_pred, 'r', label='Linear regression', linewidth=3)

    # Add line of best fit for recent years
    recent_years = df[df['Year'] >= 2000]
    slope, intercept, rvalue, pvalue, stderr = linregress(recent_years['Year'], recent_years['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(2000, 2051)])
    y_pred = slope * x_pred + intercept
    ax.plot(x_pred, y_pred, 'g', label='Linear regression (2000-2019)', linewidth=3)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Add legend and save plot
    ax.legend()
    plt.savefig('sea_level_plot.png')
    
    return ax
