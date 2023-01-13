class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            print("already")
        return cls._instance[cls]


class Singleton:
    _instance = {}

    def __init__(self):
        if Singleton._instance == None:
            Singleton._instance = self

    staticmethod
    def getinstance():
        if Singleton._instance:
            return Singleton()
        else:
            return Singleton._instance
