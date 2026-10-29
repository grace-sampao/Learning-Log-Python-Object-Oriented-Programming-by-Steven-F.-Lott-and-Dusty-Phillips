# Default values
class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.move(x, y)

# Single logical line of code expanded to multiple physical lines
class Point:
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0
    ) -> None:
        self.move(x, y)
