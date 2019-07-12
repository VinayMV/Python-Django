def percentage(total_amount,discount_amount):
    if not(type(discount_amount)==float and type(total_amount)==float):
        return ("Invalid arguments")
    if total_amount <= 0:
        return ("Invalid Case.Division by Zero is not possible!")
    return (discount_amount/total_amount)*100

def main():
    total_amount=float(input("Total amount:"))
    discount_amount=float(input("Discounted Amount:"))
    dis_p=percentage(total_amount,discount_amount)
    print("Total Amount :",total_amount,"Discount Amount:",discount_amount,"Discount%:", dis_p)

if __name__ == '__main__':
    main()
