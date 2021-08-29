"""Math operator examples and walkthrough."""

__author__ = "730390144"


lhs: str = input("Left-hand side: ")
rhs: str = input("Right-hand side: ")
exp: int = (int(lhs) ** int(rhs))
div: float = (float(lhs) / float(rhs))
othdiv: int = (int(lhs) // int(rhs))
modulo: int = (int(lhs) % int(rhs))
print(lhs + " ** " + rhs + " is " + str(exp))
print(lhs + " / " + rhs + " is " + str(div))
print(lhs + " // " + rhs + " is " + str(othdiv))
print(lhs + " % " + rhs + " is " + str(modulo))