class Author:
    def __init__(self, id, name:str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_value):
        self._id = id_value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not hasattr(self, '_name'):
            if new_name and isinstance(new_name, str):
                self._name = new_name
            else:
                raise ValueError("Name must be a non-empty string")
        else:
            raise AttributeError("Name cannot be changed after initialization")
