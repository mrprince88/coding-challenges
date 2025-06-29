from enum import Enum

class TokenType(Enum):
    STRING = "STRING"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    NULL = "NULL"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    LEFT_BRACKET = "["
    RIGHT_BRACKET = "]"
    COLON = ":"
    COMMA = ","
    EOF="EOF"
    
class Token:
    def __init__(self, token_type: TokenType, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, {self.value})"

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return self.token_type == other.token_type and self.value == other.value