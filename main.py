#Weather Man Python Project
from monthly_avg import MonthlyAverage
from monthly_graph import MonthlyGraph
from yearly_max import YearlyMax


def display_one():
	year=input("Please Enter the Year: ")
	if len(year)==4:
		op1=MonthlyAverage(year)
	else:
		print("Wrong input!! Please enter year in YYYY format!")
def display_two():
	data=input("Please Enter the year/month: ")
def display_three():
	data=input("Please Enter the year/month: ")
def display_four():
	data=input("Please Enter the year/month: ")

def main():

	print("======================================= Welcome to Weather Man ====================================================\n")
	print("1 - Display the highest temperature and day, lowest temperature and day, most humid day and humidity")
	print("2 - Display monthly average of highest temperature, average of lowest temperature, average humidity")
	print("3 - Display monthly the highest and lowest temperature on each day. Highest in red and lowest in blue")
	print("4 - Display monthly the highest and lowest temperature on each day. In same line Highest in red and lowest in blue.\n")
	print("======================================= Welcome to Weather Man ====================================================\n")
	user_option=int(input("Enter your option: "))
	if user_option==1:
		display_one()
	elif user_option==2:
		display_two()
	elif user_option==3:
		display_three()
	elif user_option==4:
		display_four()
	else:
		print("Please input valid option!!")

if __name__ == "__main__":
    main()
