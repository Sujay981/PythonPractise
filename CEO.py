dict ={
    "H":["Emp ID  -17","Emp Name - H", "CEO No manager"],
    "A":["Emp ID  -17","Emp Name - A", "Emp Manager - H"],
    "B":["Emp ID  -19","Emp Name - B", "Emp Manager - A"],
    "C":["Emp ID  -18","Emp Name - C", "Emp Manager - B"],
    "D":["Emp ID  -21","Emp Name - D", "Emp Manager - C"],
    "E":["Emp ID  -45","Emp Name - E", "Emp Manager - D"],
    "F":["Emp ID  -13","Emp Name - F", "Emp Manager - E"]
}
#details of employee till CEO
def employee_details(s):
	print(dict.get(s))
	if(s == "H"):
		print("You have reached the CEO")
	else:
		li=dict.get(s)
		#str = (string)li[2]
		st = li[2].split(' ')
		s =st[len(st)-1]
		employee_details(s)

s =input("Enter the employe name - " ,)
employee_details(s)
#print(dict.get(s))
