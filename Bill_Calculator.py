"""
step 1:
    get user's bill total
step 2:
    get user's desired gratuity percentage
step 3:
    multiply total bill amount by user's desired gratuity percentage converted into a decimal (float)
step 4:
    display original bill, gratuity percentage entered, actual gratuity, and total bill after gratuity
"""

def get_bill():
    user_bill = float(input("Enter your bill subtotal: "))
    # user_bill = "{:.2f}".format(user_bill)
    return user_bill

def get_gratuity(bill):
    gratuity = float(input("Enter the percentage gratuity you would like to add to your bill: "))
    # gratuity = "{:.2f}".format(gratuity) 
    return gratuity

def calc_gratuity(bill, gratuity):
       gratuity_amount = bill * (gratuity / 100)
       return gratuity_amount

def total_bill(bill, gratuity):
    final_bill_total = bill + gratuity
    return final_bill_total

def main():
    bill = get_bill()
    gratuity = get_gratuity(bill)
    calculated_gratuity = calc_gratuity(bill, gratuity)
    bill_total = "{:.2f}".format(total_bill(bill, calculated_gratuity))


    print(f"\n\nYour final bill was: ${bill}")
    print(f"You decided on a {gratuity}% gratuity.")
    print(f"Your gratuity is a total of ${calculated_gratuity}.")
    print(f"Your final bill total is equal to: ${bill_total}")

main()