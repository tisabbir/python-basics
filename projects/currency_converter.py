def currency_converter():
    print("This is Currency Converter!")
    usd_rate = 121.91

    amount = float(input("Enter the amount in BDT: "))
    converted_amount = amount / usd_rate
    print(f"{amount} BDT is equal to {converted_amount:.2f} USD.")

currency_converter()