print('Welcome to TipCalaculator')

bill = float(input('what was the total bill?\n'))
tip = int(input('How much tip would you like to give? 10, 12 or 15?\n'))
num = int(input('How many people to split the bill?\n'))

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill_amount = bill + total_tip_amount
bill_per_person = total_bill_amount / num

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
