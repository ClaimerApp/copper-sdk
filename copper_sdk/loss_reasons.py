class LossReasons:

    def __init__(self, copper):
        self.copper = copper

    def get(self):
        return self.copper.get(f'/loss_reasons')
