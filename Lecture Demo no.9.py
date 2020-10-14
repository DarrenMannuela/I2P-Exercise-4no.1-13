first_tax = 0
second_tax = 10/100
final_tax = 20/100


def taxable_income(income):
    final_income = income-20000
    tax_for_income = 10000*first_tax+10000*second_tax+final_income*final_tax
    return tax_for_income


print(taxable_income(45000))
