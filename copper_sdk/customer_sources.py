class CustomerSources():
    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f'/customer_sources')
