class Object:
    def __init__(self, klass, fields):
        self.klass = klass
        self.fields = fields

    def __str__(self):
        return self.klass + "(" + str(self.fields) + ")"