class MonthlyAverage:
    def __init__(self, data):
        self.data = data

    def get_monthly_average(self, year, month):
        month_data = [d for d in self.data if d["Date"].year == year and d["Date"].month == month]

        if not month_data:
            print("\n\n-------------------------------------------------\n")
            print(f"No data for {year}-{month:02d}")
            print("\n-------------------------------------------------\n\n")
            return

        highs = [int(d["Max TemperatureC"]) for d in month_data if d["Max TemperatureC"].strip()]
        lows  = [int(d["Min TemperatureC"]) for d in month_data if d["Min TemperatureC"].strip()]
        hums  = [int(d[" Mean Humidity"]) for d in month_data if d[" Mean Humidity"].strip()]

        print(f"\n\n---------------Data for {year}-{month:02d}---------------------\n")
        print(f"Highest Average: {round(sum(highs)/len(highs))}C")
        print(f"Lowest Average: {round(sum(lows)/len(lows))}C")
        print(f"Average Humidity: {round(sum(hums)/len(hums))}%")
        print("\n-------------------------------------------------\n\n")    