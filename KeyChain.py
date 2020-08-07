from enum import Enum
from Key import Key
class KeychainType(Enum):
    Success = "Success"
    Failure = "Failure"
    Ban = "Ban"
    Retry = "Retry"
    Custom = "Custom"

class KeychainMode(Enum):
    OR = "OR"
    AND = "AND"
class KeyChain:
    def __init__(self,Type=None,Mode=None,banOn4XX=None,banOnToCheck=None,Keys=None):
        self.Type = KeychainType.Success
        self.Mode = KeychainMode.AND
        self.Keys = []

    def CheckKeys(self):
        if self.Mode == KeychainMode.OR:
            for key in self.Keys:
                if key.CheckKey():
                    return True
            return False
        elif self.Mode == KeychainMode.AND:
            for key in self.Keys:
                if not key.CheckKey():
                    return False
            return True