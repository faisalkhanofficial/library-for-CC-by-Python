def get_days():
    try:
        return int(input("Enter number of days: "))
    except:
        print("Invalid input!")
        return None