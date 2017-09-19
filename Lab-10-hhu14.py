
# coding: utf-8

# In[ ]:

## Honglie Hu, hhu14@earlham.edu, white, Lab 10-A,T,C,what? 
## GC content: the calculated value is 34%, and the published value is 36.5% 


# In[1]:

## the file: sequence-1.dat

def composition(factor,sumLength,text):
    times=[]
    for i in text:
        time=i.count(factor)
        times.append(time)
    timeS=sum(times)
    Thecomposition=timeS/sumLength*100
    return(round(Thecomposition))



def main():
    filename = input("file_name:")
    file = open(filename,"r")
    fileRead = file.readlines()
    text=[]
    for line in fileRead:
        if line[0]==">":
            fileRead.remove(line)
    for line in fileRead:
            str2=line.rstrip('\n')
            text.append(str2)
    length=[]
    for i in text:
        lenz=len(i)
        length.append(lenz)
    sumLength=sum(length)
    print("Number of fragment:",len(length))
    print("Longest fragment:",max(length))
    print("Shortest fragment:",min(length))
    print("Average fragment:",sumLength/len(length))
    print("Total bases:",sumLength)

    A=composition("A",sumLength,text)
    T=composition("T",sumLength,text)
    C=composition("C",sumLength,text)
    G=composition("G",sumLength,text)
    N=composition("N",sumLength,text)
    
    print("Base composition:")
    print("A - ",A,"%")
    print("T - ",T,"%")
    print("C - ",C,"%")
    print("G - ",G,"%")
    print("N - ",N,"%")
    print("GC content - ",G+C,"%")
     
main()


# In[1]:

## the file: Pbar_1.0_scaffolds.fa

def composition(factor,sumLength,text):
    times=[]
    for i in text:
        time=i.count(factor)
        times.append(time)
    timeS=sum(times)
    Thecomposition=timeS/sumLength*100
    return(round(Thecomposition))



def main():
    filename = input("file_name:")
    file = open(filename,"r")
    fileRead = file.readlines()
    text=[]
    for line in fileRead:
        if line[0]==">":
            fileRead.remove(line)
    for line in fileRead:
            str2=line.rstrip('\n')
            text.append(str2)
    length=[]
    for i in text:
        lenz=len(i)
        length.append(lenz)
    sumLength=sum(length)
    print("Number of fragment:",len(length))
    print("Longest fragment:",max(length))
    print("Shortest fragment:",min(length))
    print("Average fragment:",sumLength/len(length))
    print("Total bases:",sumLength)

    A=composition("A",sumLength,text)
    T=composition("T",sumLength,text)
    C=composition("C",sumLength,text)
    G=composition("G",sumLength,text)
    N=composition("N",sumLength,text)
    
    print("Base composition:")
    print("A - ",A,"%")
    print("T - ",T,"%")
    print("C - ",C,"%")
    print("G - ",G,"%")
    print("N - ",N,"%")
    print("GC content - ",G+C,"%")
     
main()

