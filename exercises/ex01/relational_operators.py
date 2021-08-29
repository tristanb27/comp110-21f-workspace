"""Relationship operators program."""

__author__ = "730390144"

lhs2: str = input("Left-hand side: ")
rhs2: str = input("Right-hand side: ")
grthan: bool = lhs2 < rhs2 
greqto: bool = lhs2 >= rhs2 
eqto: bool = lhs2 == rhs2
exeq: bool = lhs2 != rhs2
print(lhs2 + " < " + rhs2 + " is " + str(grthan))
print(lhs2 + " >= " + rhs2 + " is " + str(greqto))
print(lhs2 + " == " + rhs2 + " is " + str(eqto))
print(lhs2 + " != " + rhs2 + " is " + str(exeq))