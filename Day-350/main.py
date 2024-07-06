import pandas as pd

class web_traffic_data:
    def analayzie(self):
        website_traffic_data = {
            'Visit Id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'Page': ['Homepage','Product Page','Blog Post','Contact Us','Homepage','Product Page','Blog Post','Contact Us', 'Contact Us', 'Home Page'],
            'source': ['Direct', 'Organic', 'Referral', 'Social','Direct', 'Organic', 'Referral', 'Social', 'Social', 'Referral'],
            'Duration (seconds)': [300, 600, 200, 100, 400, 350, 250, 150, 50, 500],
        }
        df = pd.DataFrame(website_traffic_data)

        total_visits = df['Visit Id'].count()
        avrage_duration = df['Duration (seconds)'].mean()
        top_3_pages_by_visit = df.nlargest(3, 'Visit Id')['Page']
        visits_by_source = df.groupby('source')['Page'].count()

        print(f'Total Visits: {total_visits}\nAvrage Duration: {avrage_duration}\nTop 3 pages by Visits: {top_3_pages_by_visit}\nVisits By source: {visits_by_source}')


if __name__ == "__main__":
    wtd = web_traffic_data()
    wtd.analayzie()