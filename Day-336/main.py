import pandas as pd
import matplotlib.pyplot as plt 

class Analyzing_Website_Traffic_Data:
    def data_sumarry(self):
        website_traffic_data = {
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Page Views': [150, 200, 180, 220, 210],
            'Unique Visitors': [100, 150, 120, 160, 155],
            'Bounce Rate': [50, 40, 45, 35, 38]
        }

        df = pd.DataFrame(website_traffic_data)

        total_page_views = df['Page Views'].sum()
        total_unique_views = df['Unique Visitors'].sum()
        avrg_bonuce_rate = df['Bounce Rate'].mean()
        higest_page_view = df.loc[df['Page Views'].idxmax()]['Date']
        lowest_page_view = df.loc[df['Bounce Rate'].idxmin()]['Date']
        print(f"Total Page View: {total_page_views}\nTotal Unique Page View: {total_unique_views}\nAvrage Bonuce Rate: {avrg_bonuce_rate}\nHighest Page view: {higest_page_view}\nLowest Page View: {lowest_page_view}")
        # Plotting Page Views over Time
        df['Page Views'].plot(title='Page Views Over Time')
        plt.xlabel('Date')
        plt.ylabel('Page Views')
        plt.show()

        # Plotting Unique Visitors over Time
        df['Unique Visitors'].plot(title='Unique Visitors Over Time')
        plt.xlabel('Date')
        plt.ylabel('Unique Visitors')
        plt.show()

        # Plotting Bounce Rate over Time
        df['Bounce Rate'].plot(title='Bounce Rate Over Time')
        plt.xlabel('Date')
        plt.ylabel('Bounce Rate (%)')
        plt.show()