import numpy as np


def hello_world() -> None:
    """Print 'Hello World'."""
    print(np.array([0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x57, 0x6F, 0x72, 0x6C, 0x64], dtype=np.byte).tobytes().decode("ASCII"))
