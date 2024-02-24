
#Singleton technique
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

first_class = Singleton()
print(first_class)

second_class = Singleton()
print(second_class) #Ts the seem first class