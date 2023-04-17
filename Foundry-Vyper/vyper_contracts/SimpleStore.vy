
val: uint256

@external
def __init__(_val: uint256):
    self.val = _val


@external
def store(_val: uint256):
    # @Jade:BINARY_OP
    self.val = _val + 5

@external
def get() -> uint256:
    return self.val
