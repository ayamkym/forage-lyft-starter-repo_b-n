# main.py
from datetime import date
from carfactory import CarFactory

def main():
    car1 = CarFactory.create_calliope(date.today(), date(2021, 6, 1), 35000, 10000)
    car2 = CarFactory.create_palindrome(date.today(), date(2021, 6, 1), True)

    print(f"Car 1 needs service: {car1.needs_service()}")
    print(f"Car 2 needs service: {car2.needs_service()}")

if __name__ == "__main__":
    main()
