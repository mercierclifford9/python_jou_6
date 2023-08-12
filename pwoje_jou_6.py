
while(True):
    try:
        x=int(input("Antre kantite not wap kalkile mwayenn lan\n"))
        break
    except ValueError:
        print("kantite enkorek, Antre kantite not wap kalkile mwayenn lan\n")
while (x<1 or x>50):
    x=int(input("kantite enkorek, Antre kantite not wap kalkile mwayenn lan\n"))
somm=0
for i in range(0,x):
    y=float(input("Antre not nimero " + str(i+1) +"\n"))
    somm=somm + y
moy=somm/x
print("Mwayenn lan se : " + str(moy))
if (moy>=90):
    print("A")
elif(moy>=80):
    print("B")
elif(moy>=70):
    print("C")
elif(moy>=60):
    print("D")
else:
    print("F")
