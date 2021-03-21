
class Result:
    
    def __init__(self, status=0, message='Success', data={}):
        self.status = status
        self.message = message
        self.data = data
    
    def __str__(self):
        return '{} - {} - {}'.format(self.status, self.message, self.data)
