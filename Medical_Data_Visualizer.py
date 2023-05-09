import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def draw_cat_plot():
    # Import data
    df = pd.read_csv('medical_examination.csv')

    # Add 'overweight' column
    df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

    # Normalize data
    df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
    df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

    # Draw cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    plt.figure(figsize=(15, 10))
    sns.catplot(data=df_cat, x='variable', kind='count', hue='value', col='cardio')
    plt.show()


def draw_heat_map():
    # Import data
    df = pd.read_csv('medical_examination.csv')

    # Clean the data
    df = df[(df['ap_lo'] <= df['ap_hi']) &
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()
