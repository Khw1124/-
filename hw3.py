def get_fixed_price(dis_price) :
    price=dis_price*100/(100-discount)
    return price

discount = int(input("할인율은?"))
a_price = get_fixed_price(int(input("A 상품의 할인된 가격은?")))
b_price = get_fixed_price(int(input("B 상품의 할인된 가격은?")))
print("A 상품의 정가는",int(a_price),"원")
print("B 상품의 정가는",int(b_price),"원")
