

class Rate():
    def __init__(self, date, base, quote, rate):
        self.date = date
        self.base = base
        self.qoute = quote
        self.rate = rate
    

class Currency():
    def __init__(self, iso_code, iso_numeric, name, symbol):
        self.iso_code = iso_code 