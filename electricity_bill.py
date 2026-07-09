name = input("Enter Your Name : ")
units = float(input("Enter number of electricity units consumed : "))
days_late = int(input("How many days late they paid the bill : "))
is_senior = input("Are You a Senior Citizen (Yes/No) : ").strip().lower()

# Validation
if units < 0 or days_late < 0:
    print("Invalid Input! (Check Units/Late Days)")

else:
    # Base Bill Calculation
    if 0 <= units <= 100:
        Base = units * 5
    elif 101 <= units <= 300:
        Base = units * 7
    elif units > 300:
        Base = units * 10
    else:
        print("Invalid input!")
        exit()

    # Senior Discount
    if is_senior == "yes":
        after_SD = Base * 0.10   # 10% discount
        s_total = Base - after_SD
    elif is_senior == "no":
        s_total = Base           # no discount
    else:
        print("Invalid Senior Citizen Input! Use Yes or No")
        exit()

    # Penalty
    late_penalty = (s_total * 0.02) * days_late

    # Final Total
    Total = s_total + late_penalty

    # Output
    print("\n--- Electricity Bill Summary ---")
    print("User Name:", name)
    print("Units Consumed:", units)
    print("Base Amount:", Base)
    print("Late Penalty:", late_penalty)
    print("Final Bill Amount (after discounts/penalty):", Total)
    print("Have a Good Day !")
