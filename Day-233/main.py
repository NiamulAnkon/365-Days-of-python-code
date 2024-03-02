#Exercise-dsa-1
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


#Monthly exzpense
monthly_expense = [2200, 2350, 2600, 2130, 2190]

#solution of number 1
comp = monthly_expense[1] - monthly_expense[0]
print(f"You have spent extra {comp} dollars")

#solution of numbr 2

tot_quart_expense = monthly_expense[0] + monthly_expense[1] + monthly_expense[2]
print(f"total expense in first quarter {tot_quart_expense} dollars")

#solution of number 3

for i in range(len(monthly_expense)):
    if i == 2000:
        print(i)
    else:
        print("No 2000 dollars spent on any month")
        break


#solution of number 4
monthly_expense.append(1980)
print(monthly_expense)

#solution of number 5
monthly_expense[3] -= 200
print(monthly_expense)