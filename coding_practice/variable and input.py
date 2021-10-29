#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("3/2 = ", 3/2)
print("3/2 = ", 3//2)
print("3/2 = ", 3%2)


# In[18]:


print("10 + 5 =", 10+5)
print("10 - 5 =", 10-5)
print("10 * 5 =", 10*5)
print("10 / 5 =", 10/5)
print("10 // 5 =", 10//5)
print("10 % 5 =", 10%5); print("; end of line")


# In[23]:


num = 100
num += 10
num += 20
print("num =", num)

str = "abcd"
str += "test"
str *= 2
print("str :", str) 


# In[35]:


str = input("문자열 입력 >")
print(str)
#print(str[0], str[-1])

s_len = len(str)
print(s_len, str[0], str[s_len -1])
print(type(str))

