
# coding: utf-8

# In[39]:


capacity = int(input())
f,fault,top,hit = [],0,0,0
s = list(map(int,input().strip().split()))

for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%capacity

        fault += 1
    else:
        hit+=1

print(fault,(hit/len(s)))


# In[38]:


capacity = int(input())
f,st,fault,hit = [],[],0,0
s = list(map(int,input().strip().split()))
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
            st.append(len(f)-1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
      
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
        hit+=1
       
print(fault,(hit/len(s))*100)


# In[41]:


capacity = int(input())
f,fault = [],0

s = list(map(int,input().strip().split()))

occurance = [None for i in range(capacity)]

for i in range(len(s)):
    if s[i] not in f:
        if len(f)<capacity:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i+1:]:
                    f[x] = s[i]
                    break
                else:
                    occurance[x] = s[i+1:].index(f[x])
            else:
                f[occurance.index(max(occurance))] = s[i]
        fault += 1


print(fault,(fault/len(s))*100)

