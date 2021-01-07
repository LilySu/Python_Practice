class OrderPizza:
    def __init__(self, location):
        self.location = location

    def sizes(self, size_request):
        if size_request == "large":
            print("24 in pizza")
        elif size_request == "medium":
            print("18 in pizza")
        elif size_request == "small":
            print("12 in pizza")
        else:
            print("Please indicate small, medium or large.")
            
    def topping(self, topping_request):
        if topping_request == "pepperoni":
            print("pepperoni coming right up")
        elif topping_request == "plain":
            print("plain pizza coming right up")
        elif topping_request == "sausage":
            print("sausage coming right up")
        else:
            print("What topping would you like?")

    def order_contents(self):
        return self.size, self.topping

    header = "Oo----------------oO"
    footer = "Oo----------------oO \n Oo----------oO"

    def apply_template(self):
        print(self.header)
        print(self.order_contents())
        # print(self.footer)

    @classmethod
    def finalize_template(cls, template):
        cls.header = template


if __name__ == '__main__':
    order = OrderPizza('dominos')
    order.sizes("medium")
    order.topping("pepperoni")
    order.finalize_template("Xx----xX")
    order.apply_template()