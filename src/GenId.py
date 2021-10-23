from datetime import datetime


class GenId:
    def __init__(self, node_id):
        self.node_id = node_id
        self.counter = 0

    def get_id(self):
        return f'{str(self.node_id).zfill(2)}{str(self.counter).zfill(8)}'
    
    def next_id(self):
        self.counter += 1
        return f'{str(self.node_id).zfill(2)}{str(self.counter).zfill(8)}'