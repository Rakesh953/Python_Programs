    # Custom/User Exceptin

class StudentError(Exception):
    def __init__(self,smg):
        self.smg=smg
    def __str__(self):
        return self.smg
raise StudentError('Not lestining to class')