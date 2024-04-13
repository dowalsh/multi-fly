class Location:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    


 