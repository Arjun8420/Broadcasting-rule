#Broadcasting rule
#Rule is = consider, a1=(m,n)
#                    a2=(p,q)
# m=p or m or p = 1
# n=q or n or q = 1

import numpy as np

a1 = np.array([[1,2,3],
              [4,5,6]])
a2 = np.array([7,8,9])
a3 = np.array([[1,2],
               [7,9]])
a4 = np.array([[10],
               [11],
               [12]])

print(np.add(a1,a2))
print(np.add(a2,a4))

#Code throws an error because the rule does not satisfies

#print(np.add(a1,a3))
#print(np.add(a1,a4))
