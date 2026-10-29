stock_name = "Apple"
number_of_shares = 10
purchase_price = 150
new_share_price = 175

total_investment_cost = number_of_shares * purchase_price

current_investment_value = number_of_shares * new_share_price

profit_or_loss = current_investment_value - total_investment_cost

percentage_return = (profit_or_loss / total_investment_cost) * 100

print("Stock:", stock_name)
print("Number of Shares:", number_of_shares)
print("Purchase Price per Share: $", purchase_price)
print("Total Investment Cost: $", total_investment_cost)
print("New Share Price: $", new_share_price)
print("Current Investment Value: $", current_investment_value)
print("Profit or Loss: $", profit_or_loss)
print("Percentage Return:", round(percentage_return, 2), "%")