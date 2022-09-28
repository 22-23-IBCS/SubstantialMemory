class coffeeShop:
    def __init__(self,n,v,b,c,p):
        self.name = n
        self.volume = v
        self.brand = b
        self.customer = c
        self.price = p

    def getPrice(self):
        return self.price

    def getCustomer(self):
        return self.customer

def main():
    print("Hi, welcome to Joseph and Charles cofee shop. Please pick an option")
    x= int(input("What would you like to order\n1.coffee\n2.latte\n3.hot cider\n"))
    if x == 1:
        cbrand = input("what coffee brand would you like\n")
        customer = input("name for the order?\n")
        coffeeorder = coffeeShop("coffee","16 oz", cbrand, customer, "3.00")
        print("Your order is " + cbrand + " " + coffeeorder.name + " for " + coffeeorder.getCustomer() + ". It will be " + coffeeorder.getPrice())
        print("Here you go. Come again!")
    
    elif x == 2:
        lbrand = input("what latte brand would you like\n")
        print("Alright, a " + lbrand + " latte")
        customer = input("name for the order?\n")
        print("ok, for " + customer)
        coffeeorder = coffeeShop("latte","8 oz", lbrand, customer, "3.00")
        print("Your order is " + lbrand + " " + coffeeorder.name + " for " + coffeeorder.getCustomer() + ". It will be " + coffeeorder.getPrice())
        print("Here you go. Come again!")
    elif x == 3:
        hcbrand = input ("what hot cider brand would you like\n")
        customer = input("name for the order?\n")
        coffeeorder = coffeeShop("hot cider","24 oz", hcbrand, customer, "3.00")
        print("Your order is " + hcbrand + " " + coffeeorder.name + " for " + coffeeorder.getCustomer() + ". It will be " + coffeeorder.getPrice())
        print("Here you go. Come again!")
    else:
        print("sorry we dont have that :(")
    
if __name__ == "__main__":
    main()    
