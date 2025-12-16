# Scenario
# An e-commerce order goes through multiple states.
# Rules
# Order class:
# order_id, items, status
# Valid status flow:
#  CREATED → PAID → SHIPPED → DELIVERED
# Invalid transitions should raise exception
# Cancel allowed only before SHIPPED
# Implement:

# update_status(new_status)

# cancel_order()



class Order:
    def __init__(self, id, status = "CREATED"):
        self.id = id
        self.status = status
        self.items = []
    
    def validate_Status_flow(self, status):
        if self.status == "CREATED" and status == "PAID":
            return True
        elif self.status == "PAID" and status == "SHIPPED":
            return True
        elif self.status == "SHIPPED" and status == "DELIVERED":
            return True
        else:
            return False
    
    def updateStatus(self, status):
        if self.validate_Status_flow(status):
            self.status = status
            print("updated status")
        else:
            print("Invalid transitions")
            
class Order1(Order):
    def validate_Status_flow(self):
        return -1





s1 = Order(1)
s1.updateStatus("PAID")
s1.updateStatus("SHIPPED")
s1.updateStatus("DELIVERED")



s2 = Order1(2)
print(s2.validate_Status_flow())