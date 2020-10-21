def is_matching(s) -> bool:
    while len(s)>0:
        l=len(s)
        s=s.replace('()','').replace('{}','').replace('[]','')
        if l==len(s):return False
    return True
value =input()
s=""
t=""
for val in value:
    if(val == '(' or val == ')' or val == '[' or val == ']' or val == '{' or val == '}'):
        s= s+val
    else:
        t=t+val if(val != ' ') else t
b = is_matching(s)
def  is_and_or(ch):
    output = ""
    if(ch == "||"):
        output = "or"
    else:
        output = "and" #assuming the given format has either || or &&
    return output
if(b):
    #assuming there is a always two innner and outer operation
    mid = is_and_or(t[8:10])
    m2 = is_and_or(t[13:15])
    m1 = is_and_or(t[3:5])
    print ('''  query:[
                    {0}:[
                         [
                            {1}: [
                                {2},
                                {3}
                                 ]
                        ],
                            [
                            {4}:[
                                {5}
                                {6}
                                ]
                            ]
                        ]
                        ]''' .format(mid,m1,t[0:3],t[5:8],m2,t[10:13],t[15:]))
else:
    print("Syntax invalid")
