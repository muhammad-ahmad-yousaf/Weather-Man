from colorama import Fore, Style, init
init(autoreset=True)

class MonthlyGraph:
    def __init__(self, data):
        self.data = data

    def monthly_bar_chart(self, year, month, combined=False):
        month_data = [d for d in self.data if d["Date"].year == year and d["Date"].month == month]

        if not month_data:
            print("\n-------------------------------------------------\n\n")
            print(f"No data for {year}-{month:02d}")
            print("\n-------------------------------------------------\n\n")
            return

        print(f"\n{month_data[0]['Date'].strftime('%B %Y')}")
        for d in month_data:
            if not d["Max TemperatureC"].strip() or not d["Min TemperatureC"].strip():
                continue  
            try:
                high = int(d["Max TemperatureC"])
                low  = int(d["Min TemperatureC"])
            except ValueError:
                continue 
            day = d["Date"].day
            if combined:
                print(f"{day:02d} {Fore.BLUE}{'+'*low}{Style.RESET_ALL}{Fore.RED}{'+'*high}{Style.RESET_ALL} {low}C - {high}C")
            else:
                print(f"{day:02d} {Fore.RED}{'+'*high}{Style.RESET_ALL} {high}C")
                print(f"{day:02d} {Fore.BLUE}{'+'*low}{Style.RESET_ALL} {low}C")
        print("\n\n")
