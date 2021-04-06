f = open("input.txt","r")
content = f.read().split("\n")
sigma = []
states = []
transitions = []
for i in range(len(content)):
    if content[i]=="Sigma:":
        for j in range(i+1,len(content)):
            if content[j]=="End":
                break
            else:
                sigma.append(content[j])
    if content[i]=="States:":
        for j in range(i+1,len(content)):
            if content[j]=="End":
                break
            else:
                states.append(content[j])
    if content[i]=="Transitions:":
        for j in range(i+1,len(content)):
            if content[j]=="End":
                break
            else:
                transitions.append(content[j])

count_s = 0
count_f = 0
for i in range(len(states)):
     state_s_f = states[i].split(" , ")
     if len(state_s_f) >1 :
         if len(state_s_f)==2:
             if state_s_f[1] == 'S':
                 count_s+=1
             if state_s_f[1] == 'F':
                 count_f+=1
         if len(state_s_f) == 3:
             if state_s_f[1] == 'S' or state_s_f[2]=='S':
                 count_s+=1
             if state_s_f[1] == 'F' or state_s_f[2]=='F':
                 count_s+=1

if count_s!=1:
    validate = False
elif count_f<1:
    validate = False
else:
    validate = True
print(validate)

            


    
