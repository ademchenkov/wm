class Exceptions:
    def __init__(self):
        self.exceptions = {}

    def add_exception(self, model_name, code, text):
        if model_name not in self.exceptions:
            self.exceptions[model_name] = {}
        self.exceptions[model_name][code] = text

    def get_exception_text(self, model_name, code):
        return self.exceptions.get(model_name, {}).get(code, '')