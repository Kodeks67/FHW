class Counter:
    def __init__(self):
        self._count = 0

    def add(self):
        self._count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("An exception occurred:", exc_type, exc_value)
            return False
        else:
            print("Exiting the resource block")
            return True
