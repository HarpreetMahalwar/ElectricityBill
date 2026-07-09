# ============================================
# Electricity Bill Calculator
# Created by Harpreet Mahalwar
# ============================================

try:
    #First things first... who's paying the bill? 
    name = input("Enter Your Name: ").strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    # Let's see how much electricity you consumed.
    units = float(input("Enter number of electricity units consumed: "))

    if units < 0:
        raise ValueError("Units cannot be negative.")

    # Modi doesn't forget late payments.
    days_late = int(input("How many days late was the bill paid: "))

    if days_late < 0:
        raise ValueError("Late days cannot be negative.")

    # Senior citizens get some respect and a discount.
    is_senior = input("Are You a Senior Citizen? (Yes/No): ").strip().lower()

    if is_senior not in ["yes", "no"]:
        raise ValueError("Please enter only 'Yes' or 'No'.")

    if units <= 100:
        base_amount = units * 5

    elif units <= 300:
        base_amount = units * 7

    else:
        base_amount = units * 10

    # Discount for Senior citizens
    if is_senior == "yes":
        discount = base_amount * 0.10
    else:
        discount = 0

    amount_after_discount = base_amount - discount

    # Every late day makes the bill a little heavier.
    late_penalty = amount_after_discount * 0.02 * days_late

    total_bill = amount_after_discount + late_penalty

    print("\n========== Electricity Bill ==========")
    print(f"Customer Name        : {name}")
    print(f"Units Consumed       : {units}")
    print(f"Base Amount          : ₹{base_amount:.2f}")
    print(f"Senior Discount      : ₹{discount:.2f}")
    print(f"Late Penalty         : ₹{late_penalty:.2f}")
    print("--------------------------------------")
    print(f"Final Bill Amount    : ₹{total_bill:.2f}")
    print("======================================")
    print("Thank you! Have a nice day. 😊")

except ValueError as e:
    # Ooh MC Something wasn't entered correctly.
    print(f"\nInput Error: {e}")

except Exception as e:
    #If you're seeing this, even I didn't expect it.
    print(f"\nUnexpected Error: {e}")

                # Developer : Harpreet Mahalwar
                # Instagram : @mahalwarharpreet
                # Date of last update : 17/03/2025
                
