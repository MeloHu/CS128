
# coding: utf-8

# In[1]:

def main():
    filename = input("file_name:")
    file = open(filename,"r")
    fileRead = file.readlines()
    text=[]

    for line in fileRead:
            str2=line.rstrip('\n')
            text.append(str2)
                
    label=[]        
    for line in text:
        if line[0]==">":
            str3=line.lstrip('>')+','
            label.append(str3)
    
    number=-1
    str4=''
    scaffold=[]
    for i in text:
        if i[0]==">":
            print(str4)
            number=number+1
            str4=label[number]
        else:    
            str4=str4+i
    print(str4)

main()


# In[2]:

def main():
    filename = input("file_name:")
    file = open(filename,"r")
    fileRead = file.readlines()
    text=[]

    for line in fileRead:
            str2=line.rstrip('\n')
            text.append(str2)
                
    label=[]        
    for line in text:
        if line[0]==">":
            str3=line.lstrip('>')+','
            label.append(str3)

    number=-1
    str4=''
    scaffold=[]
    for i in text:
        if i[0]==">":  
            scaffold.append(str4)
            number=number+1
            str4=label[number]
        else:    
            str4=str4+i
    scaffold.append(str4)
    del scaffold[0]
    print(scaffold)

main()


# In[ ]:



