class InvalidError(Exception):
    def _init__(self, message):
        self.message = message

try:
    char = input()
    if(len(char)>1):
        raise InvalidError("More than one character available")
    print(ord(char))

except InvalidError as e :
    print(e)