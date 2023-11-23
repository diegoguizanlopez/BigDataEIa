"""
Excepción personalizada con salidas personalizadas
"""

class PersonalizedException(Exception):

    def __init__(self, message, errors):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
            
        # Now for your custom code...
        self.errors = errors

    def getErrorMessage(self):
        print(f"\033[91m ERRROR : {self.errors} : {self.message}\033[0m")

    