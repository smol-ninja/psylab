class CustomValueError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}
try:
    raise CustomValueError("Value must be within 1 and 10.")
except CustomValueError as e:
    print("CustomValueError Exception!", e.strerror)
