

class Singleton(type):
    """This class can be used as metaclass for ensuring that a class has only one instance"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        returns existing class instance if it exists
        ---
        Params:
            cls: class which is being instansiated
        ---
        Returns:
            if class instance exists, return that instance, otherwise return new instance
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]