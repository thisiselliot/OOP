class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.emp_discount = emp_discount
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        self.items += [{name: price}] * quantity
        self.total += price*quantity
        print(self.total)
    
    def mean_item_price(self):
        print(self.total / len(self.items))

    def median_item_price(self):
        print(
            sum(sorted([[item[1] for item in item.items()] for item in self.items])[len(self.items)//2]
            + sorted([[item[1] for item in item.items()] for item in self.items])[len(self.items)//2-(len(self.items)%2==0)]) / 2
        )

    def apply_discount(self):
        if self.emp_discount:
            self.total -= self.total * self.emp_discount / 100
            print(self.total)
        else:
            print("Sorry, there is no discount to apply to your cart :(")
       
    def void_last_item(self):
        if self.items:
            self.total -= sum([item[1] for item in self.items.pop().items()])
            self.total = round(self.total, 2)
            print(self.total)
        else:
            print("There are no items in your cart!")