import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#testing pull request

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df.set_index('date', drop=True)

# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.

df = df[
    (df['value'] > df['value'].quantile(0.025)) &
    (df['value'] < df['value'].quantile(0.975)) 
    ]

def draw_line_plot():
    # Draw line plot
    # Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
    # The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. 
    # The label on the x axis should be Date and the label on the y axis should be Page Views.
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['value'])
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

     # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". 
    # It should show average daily page views for each month grouped by year. 
    # The legend should show month labels and have a title of Months. 
    # On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
    df_bar = df
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df['date'].dt.year)
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    ax.set_title('Novo')
    ax.legend(title='Legenda')

    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    # fig.savefig('box_plot.png')
    # return fig
