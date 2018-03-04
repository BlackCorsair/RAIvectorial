class DBManager:
    def __init__(self):
        print("DBManager init")

    def sayHello(self, name):
        if name is "":
            print("hello world")
        else:
            print("hello ", name)
