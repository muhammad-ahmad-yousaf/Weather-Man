class YearlyMax:
	def __init__(self,data):
		self.data = data

	def get_yearly_summary(self, year):
		year_data = [d for d in self.data if d["Date"].year == year]

		if not year_data:
			print("\n-------------------------------------------------\n\n")
			print(f"No data found for year {year} !!!")
			print("\n-------------------------------------------------\n\n")
			return

		highest = max(year_data, key=lambda d: int(d["Max TemperatureC"] or -999))
		lowest = min(year_data, key=lambda d: int(d["Min TemperatureC"] or 999))
		humid  = max(year_data, key=lambda d: int(d[" Mean Humidity"] or -1))

		print(f"\n\n------------------{year} Data------------------\n")
		print(f"Highest: {highest['Max TemperatureC']}C on {highest['Date'].strftime('%B %d')}")
		print(f"Lowest: {lowest['Min TemperatureC']}C on {lowest['Date'].strftime('%B %d')}")
		print(f"Humid: {humid[' Mean Humidity']}% on {humid['Date'].strftime('%B %d')}")
		print("\n-------------------------------------------------\n\n")