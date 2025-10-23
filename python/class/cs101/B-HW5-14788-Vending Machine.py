class VendingMachine:
    class Item:
        def __init__(self, price: int, stock: int):
            self.price = price
            self.stock = stock

    def __init__(self, balance: int):
        self.items = {} 
        self.balance = balance
        self.initial_balance = balance

    def buy(self, name, quantity):
        if name in self.items:
            item = self.items[name]
            if quantity > item.stock:
                print('no stock')
                return
            
            item.stock -= quantity
            self.balance += item.price * quantity

    
    def restock(self, name, price, quantity):
        cost = (price * quantity) / 2
        if cost > self.balance:
            print('you dont have money')
            return
        
        self.balance -= cost
        if name in self.items:
            item = self.items[name]
            item.price = price
            item.stock += quantity
        else:
            self.items[name] = self.Item(price, quantity)

    def __str__(self):
        profit = self.balance - self.initial_balance
        return f"Profit: {profit}"
    
    # Continue the class

# ----- input output handler -----
line = input().split()
T = int(line[0])
initial_balance = int(line[1])
machine = VendingMachine(initial_balance)
for _ in range(T):
    parts = input().split()
    cmd = parts[0]
    if cmd == "BUY":
        name, qty = parts[1], int(parts[2])
        machine.buy(name, qty)
    elif cmd == "RESTOCK":
        name, price, qty = parts[1], int(parts[2]), int(parts[3])
        machine.restock(name, price, qty)
print(machine)
