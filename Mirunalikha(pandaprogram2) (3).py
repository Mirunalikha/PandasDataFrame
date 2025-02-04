#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
info=pd.DataFrame([[3,9]]*4,columns=['S','R'])
print("\n Original DataFrame:\n",info)
print("\n Square root:\n",info.apply(np.sqrt))
print("\n Sum of each column:\n",info.apply(np.sum,axis=0))
print("\n Sum of each row:\n",info.apply(np.sum,axis=1))


# In[1]:


import pandas as pd
import numpy as np
info=pd.DataFrame([[2,4,6],[1,3,5],[5,8,7]],columns=['X','Y','Z'])
print(info)
print(info.agg(['min','max']))


# In[5]:


import pandas as pd
import numpy as np
d2=pd.DataFrame([['Yasir',10],['Miru',20]],columns=['EmpName','ID'])
print(d2)
d2['Age']=[20,18]
print("\n Adding new column:\n",d2)
d2['Sex']=['Male','Female']
print("Adding new column:\n",d2)


# In[6]:


#to add a new column
import pandas as pd
import numpy as np
d2=pd.DataFrame([['Yasir',10],['Miru',20]],columns=['EmpName','ID'])
print(d2)
a=d2.assign(Age=[20,18])
print("Adding a new column:\n",a)


# In[10]:


import pandas as pd
import numpy as np
info=pd.DataFrame(np.random.randn(5,2),index=[3,2,0,4,1],columns=['col1','col2'])
print(info)
info2=info.sort_index()
print(info2)
info3=info.sort_values(by='col2')
print(info3)


# In[1]:


import pandas as pd
import numpy as np
left=pd.DataFrame({'id':[1,2,3,4],'Name':['Apple','Ball','Cat','Dog'],'sub':['sub1','sub2','sub4','sub3']})
right=pd.DataFrame({'id':[1,2,3,4],'Name':['Winter','Summer','Monsoon','Spring'],'sub':['sub2','sub4','sub3','sub5']})
print(left)
print(right)
print(pd.merge(left,right,on='id'))


# In[ ]:




