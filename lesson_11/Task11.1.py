class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste is None:
            return "У вас обычная газировка"
        else:
            return f"У вас газировка с {self.taste} вкусом"

strawberry = Soda("клубничным")
casual = Soda()
cucumber = Soda("огуречным")

print(casual)
print(strawberry)
print(cucumber)