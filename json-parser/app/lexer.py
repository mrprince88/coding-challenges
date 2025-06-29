from app.token import Token, TokenType

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position] if self.text else None
        
    def error(self):
        raise Exception('Invalid character')
    
    def next(self):
        self.position += 1
        self.current_char = self.text[self.position] if self.position < len(self.text) else None
    
    def peek(self, length):
        return self.text[self.position:self.position + length]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.next()
    
    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.next()
        return float(result)
    
    def string(self):
        result = ''
        if self.current_char == '"':
            self.next()  # skip opening quote
            while self.current_char is not None and self.current_char != '"':
                result += self.current_char
                self.next()
            if self.current_char == '"':
                self.next()  # skip closing quote
                return result
            else:
                self.error()
        else:
            self.error()

    def boolean(self):
        if self.peek(4) == "true":
            for _ in range(4): self.next()
            return True
        elif self.peek(5) == "false":
            for _ in range(5): self.next()
            return False
        self.error()

    def null(self):
        if self.peek(4) == "null":
            for _ in range(4): self.next()
            return None
        self.error()

    
    def next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.peek(4) == "true":
                return Token(TokenType.BOOLEAN, self.boolean())

            if self.peek(5) == "false":
                return Token(TokenType.BOOLEAN, self.boolean())

            if self.peek(4) == "null":
                return Token(TokenType.NULL, self.null())

            if self.current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())

            if self.current_char == '"':
                return Token(TokenType.STRING, self.string())

            if self.current_char == '{':
                self.next()
                return Token(TokenType.LEFT_BRACE, '{')

            if self.current_char == '}':
                self.next()
                return Token(TokenType.RIGHT_BRACE, '}')

            if self.current_char == '[':
                self.next()
                return Token(TokenType.LEFT_BRACKET, '[')

            if self.current_char == ']':
                self.next()
                return Token(TokenType.RIGHT_BRACKET, ']')

            if self.current_char == ',':
                self.next()
                return Token(TokenType.COMMA, ',')

            if self.current_char == ':':
                self.next()
                return Token(TokenType.COLON, ':')

            self.error()

        return Token(TokenType.EOF, None)

