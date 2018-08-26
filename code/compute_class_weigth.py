def compute_class_weigth(y):
    import numpy as np
    u = np.unique(y)
    r = {}
    for i in range(len(u)):
        r[i] = sum(u[0]==y)/sum(u[i]==y)
        
    return r