import pandas as pd

class analyzie_data:
    def data_summarry(self):
        data = {
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
            'Units Sold': [10, 5, 8, 15, 7],
            'Revenue': [100, 75, 80, 150, 105]
        }

        df = pd.DataFrame(data)

        total_revune = df["Revenue"].sum()
        unit_sold_total = df["Units Sold"].sum()
        avrage_revune = df['Revenue'].mean()
        print(f"The Total Revune is: {total_revune}\nThe total unit solds are: {unit_sold_total}\nThe avarge revune is: {avrage_revune}")


if __name__ == "__main__":
    ad = analyzie_data()
    ad.data_summarry()