import os

from monthly_avg import MonthlyAverage
from monthly_graph import MonthlyGraph
from yearly_max import YearlyMax


import csv
from datetime import datetime

def load_data(folder_path):
    all_data = []
    for file in os.listdir(folder_path):
        if not file.endswith(".txt"):
            continue
        file_path = os.path.join(folder_path, file)

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)

            if not rows[0]:
                rows = rows[1:]

            headers = rows[0]
            for row in rows[1:]:
                if not row or len(row) < len(headers):
                    continue  
                record = dict(zip(headers, row))
                try:
                    record["Date"] = datetime.strptime(record["PKT"], "%Y-%m-%d")
                except Exception:
                    continue
                all_data.append(record)
    return all_data
def main():
    print("1- Lahore\n2- Murree\n3- Dubai")
    city_option=int(input("Select the City: "))
    if city_option == 1:
        folder_path = "data\lahore_weather"
    elif city_option == 2:
        folder_path = "data\Murree_weather"
    elif city_option == 3:
        folder_path = "data\Dubai_weather"
    else:
        print("Please select Correct option!!")
    data = load_data(folder_path)
    yearly = YearlyMax(data)
    monthly_avg = MonthlyAverage(data)
    monthly_graph = MonthlyGraph(data)
    
    while True:
        print("======================================= Welcome to Weather Man ====================================================\n")
        print("1 - Display the highest temperature and day, lowest temperature and day, most humid day and humidity")
        print("2 - Display monthly average of highest temperature, average of lowest temperature, average humidity")
        print("3 - Display monthly the highest and lowest temperature on each day. Highest in red and lowest in blue")
        print("4 - Display monthly the highest and lowest temperature on each day. In same line Highest in red and lowest in blue.")
        print("5 - Exist\n")
        print("===================================================================================================================\n")
        user_option=int(input("Enter your option: "))
        if user_option == 1:
            year = int(input("Enter year (like 2002): "))
            yearly.get_yearly_summary(year)
        elif user_option == 2:
            year = int(input("Enter year (like 2005): "))
            month = int(input("Enter month (range 1-12): "))
        elif user_option == 3:
            year = int(input("Enter year (like 2011): "))
            month = int(input("Enter month (range 1-12): "))
            monthly_graph.monthly_bar_chart(year, month, combined=False)
        elif user_option == 4:
            year = int(input("Enter year (like 2011): "))
            month = int(input("Enter month (range 1-12): "))
            monthly_graph.monthly_bar_chart(year, month, combined=True)
        elif user_option == 5:
            print("Exiting Weather Man.")
            break
        else:
            print("Invalid option!! Try again.")

if __name__ == "__main__":
    main()
