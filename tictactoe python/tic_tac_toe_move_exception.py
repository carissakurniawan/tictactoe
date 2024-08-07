# Your exception here

# Exception for players trying to move in the box that already taken
class InvalidMoveException(Exception):
    pass


# Exception for players who trying to take spot outside range 1-9)
class InvalidKeyException(Exception):
    pass
