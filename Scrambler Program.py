#!/usr/bin/env python
# coding: utf-8

# # Scrambler Program

# In[11]:


def scramble_function(final):
    import string, random, re
    f=re.compile(r'\s')
    x=f.split(u''.join(c for c in final if c not in set(string.punctuation)))
    for i in x:
        if len(i)<4: continue
        y=list(i[1:-1])
        random.shuffle(y)
        z=u'%c%s%c' % (i[0], ''.join(y), i[-1])
        final=final.replace(i,z,1)
    return final
if __name__=='__main__':
    #Output 1
    string=input('enter the string')
    v=scramble_function(string)
    print(v)


# In[13]:


#Output 2
string=input('enter the string')
v=scramble_function(string)
print(v)


# In[ ]:




