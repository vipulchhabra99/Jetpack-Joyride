import numpy as np
a = np.array([['$','$',' ',' '],[' ',' ','$','$'],['$',' ','$',' ']])
unique,counts = np.unique(a,return_counts=True)
temp = dict(zip(unique,counts))
print(temp['$'])