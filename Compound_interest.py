P=int(input("Enter the Principle amount:"))
T=int(input("Enter the Time period:"))
R=int(input("Enter the interest rate:"))
def compound(P,T,R):
	if T==0:
		return P
	else:
		return compound(P+(P*R)/100,R,T-1)
print(compound(P,T,R))
