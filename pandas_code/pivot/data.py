import pandas as pd


def get_car_sales_df():
    return pd.DataFrame(data=[
        ['Moscow', 'jan', 'Haval', 1300],
        ['Moscow', 'feb', 'Haval', 1200],
        ['Moscow', 'mar', 'Haval', 1100],

        ['Moscow', 'jan', 'Chery', 800],
        ['Moscow', 'feb', 'Chery', 700],
        ['Moscow', 'mar', 'Chery', 600],

        ['Moscow', 'jan', 'Geely', 250],
        ['Moscow', 'feb', 'Geely', 240],

        ['St. Peterburg', 'jan', 'Haval', 900],
        ['St. Peterburg', 'feb', 'Haval', 870],
        ['St. Peterburg', 'mar', 'Haval', 850],

        ['St. Peterburg', 'jan', 'Chery', 650],
        ['St. Peterburg', 'feb', 'Chery', 640],
        ['St. Peterburg', 'mar', 'Chery', 705],

        ['St. Peterburg', 'jan', 'Geely', 120],
        ['St. Peterburg', 'feb', 'Geely', 135],
        ['St. Peterburg', 'mar', 'Geely', 145],
    ], columns=['city', 'month', 'producer', 'sales'])


if __name__ == '__main__':
    print(get_car_sales_df())
