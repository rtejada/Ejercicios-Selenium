details = [["Camisa", "De algon pima y gamusa", '20', '1'], ["Vestido", "lo que sea", '30', '2'],
           ["vaquero", "para vaqueros", '18.50', '2']]

total_price = 0
for description in details:
    price = description[2]
    quantity = description[3]
    amount = float(price) * int(quantity)
    total_price += amount

print('Importe total a pagar:', total_price)

iva = 21
importe_iva = total_price * iva / 100
print(importe_iva)

