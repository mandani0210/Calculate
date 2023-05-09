import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by filtering out the top and bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(df.index, df['value'], color='r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Prepare data for plotting
    df_bar = df.groupby([df.index.year, df.index.month])['value'].mean().unstack()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16, 6))
    df_bar.plot(kind='bar', ax=ax)
    ax.legend(title='Months', labels=df_bar.columns.map(lambda x: x.strftime('%B')))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views for each Month (2016-2019)')
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for plotting
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (year-wise and month-wise)
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    plt.savefig('box_plot.png')
    return fig
