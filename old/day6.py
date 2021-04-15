#!/usr/bin/env python
# coding: utf-8

# ### Hash table / dictonaries

# In[8]:


book = {
    "apple": 2.5,
    "mango": 12,
    "orange": 3
}

print (book ["mango"])


# In[18]:


voted ={}

def check_voter(name):
    if voted.get(name):
        print ("kick them out.")
    else:
        voted[name] = True
        print ("let them vote!")
        
name = input("Enter the name: ")
check_voter(name)
name = input("Enter the name: ")
check_voter(name)

