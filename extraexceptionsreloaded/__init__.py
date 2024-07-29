class DefaultException:
    def __init__(self, *msg) -> None:
        if msg:
            self.message = msg[0]
        else:
            self.message = ""
    
    def __str__(self) -> str:
        return self.message

from ethernetexceptions import *
from efficiency import *
