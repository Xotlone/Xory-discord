import json

class Constants:
    def __init__(self):
        with open('CONSTANTS.json') as f:
            self.json_ = json.load(f)

    def __getattr__(self, item):
        try:
            return self.json_[item]
        except KeyError:
            raise KeyError(f'constants "{item}" is not exists')

constants = Constants()
