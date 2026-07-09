print("Hello World")

class dan():
    def __init__(self) -> None:
        self.height = 1

    def get_height(self):
        return self.height


myObj = dan()

height = myObj.get_height()

print(height)
