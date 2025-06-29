from app.token import TokenType

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
        
    def error(self):
        raise Exception("Invalid Syntax")
    
    def consume(self, token_type):
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.next_token()
        else:
            self.error()
    
    def parse(self):
        return self.parse_value()
    
    def parse_value(self):
        token_type = self.current_token.token_type

        if token_type == TokenType.STRING:
            value = self.current_token.value
            self.consume(TokenType.STRING)
            return value
        
        elif token_type == TokenType.NUMBER:
            value = self.current_token.value
            self.consume(TokenType.NUMBER)
            return value
        
        elif token_type == TokenType.BOOLEAN:
            value = self.current_token.value
            self.consume(TokenType.BOOLEAN)
            return value
        
        elif token_type == TokenType.NULL:
            self.consume(TokenType.NULL)
            return None
        
        elif token_type == TokenType.LEFT_BRACE:
            return self.parse_object()
        
        elif token_type == TokenType.LEFT_BRACKET:
            return self.parse_array()
        
        else:
            self.error()
    
    def parse_object(self):
        obj = {}
        self.consume(TokenType.LEFT_BRACE)

        if self.current_token.token_type == TokenType.RIGHT_BRACE:
            self.consume(TokenType.RIGHT_BRACE)
            return obj
        
        while True:
            if self.current_token.token_type != TokenType.STRING:
                self.error()
            
            key = self.current_token.value
            self.consume(TokenType.STRING)

            self.consume(TokenType.COLON)
            value = self.parse_value()
            obj[key] = value

            if self.current_token.token_type == TokenType.COMMA:
                self.consume(TokenType.COMMA)
            elif self.current_token.token_type == TokenType.RIGHT_BRACE:
                self.consume(TokenType.RIGHT_BRACE)
                break
            else:
                self.error()
        
        return obj
    
    def parse_array(self):
        arr = []
        self.consume(TokenType.LEFT_BRACKET)

        if self.current_token.token_type == TokenType.RIGHT_BRACKET:
            self.consume(TokenType.RIGHT_BRACKET)
            return arr
        
        while True:
            value = self.parse_value()
            arr.append(value)

            if self.current_token.token_type == TokenType.COMMA:
                self.consume(TokenType.COMMA)
            elif self.current_token.token_type == TokenType.RIGHT_BRACKET:
                self.consume(TokenType.RIGHT_BRACKET)
                break
            else:
                self.error()
        
        return arr
