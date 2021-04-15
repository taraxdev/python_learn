#!/usr/bin/env python
# coding: utf-8

# In[34]:


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')


# In[35]:


app = (1,2,3,4,5,6)
p = 1
for a in app:
    p *= a
    
p


# In[37]:


s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
for char in s:
    if char.isupper():
        print(char, end="")

