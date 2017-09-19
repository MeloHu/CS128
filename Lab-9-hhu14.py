
# coding: utf-8

# In[ ]:

## Honglie Hu,hhu14@earlham.edu,Saturday&8:00 at 66.5486,-18.0233,Lab9-M&M


# In[1]:

## Part A

def main():
    filename = input("file_name:")
    file = open(filename,"r")
    text = file.read()
    length = text.split()  
    count=len(length)
    print("Count:",count)
    
    TheNumber =[float(i) for i in length]
    file.close()
    
## to get "mode"    
    mNumber = [TheNumber.count(i) for i in TheNumber]
    position = max(mNumber)
    positionArray = mNumber.index(position)
    Mode = TheNumber[positionArray]

## --------------------------------------
    
    print("Total:",sum(TheNumber))
    print("Smallest:",min(TheNumber))
    print("Largest:",max(TheNumber))
    average=sum(TheNumber)/count
    print("Mode:",Mode)
    print("Average:",average)
    

main()


# In[2]:

## Part B

def main():
    import math
    filename = input("file_name:")
    file = open(filename,"r")

    text = file.read()
    length = text.split()  
    count = len(length)
    print("Count:",count)
    
    TheNumber =[float(i) for i in length]
    file.close()
    
## to get "mode"    
    mNumber = [TheNumber.count(i) for i in TheNumber]
    position = max(mNumber)
    positionArray = mNumber.index(position)
    Mode = TheNumber[positionArray]

## ---------------------------------
    print("Total:",sum(TheNumber))
    print("Smallest:",min(TheNumber))
    print("Largest:",max(TheNumber))
    average=sum(TheNumber)/count
    print("Mode:",Mode)    
    
## to get "median"
    TheNumber.sort()
    medianNumber = len(TheNumber)
    Median =(TheNumber[math.floor(medianNumber/2)])
    print("Median:",Median)
## ----------------------------------

    print("Average:",average)
    
main()


# In[ ]:



