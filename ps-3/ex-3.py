import numpy as np

T = 1000
dt = 1 #dt in seconds

amt_Bi213 = 10000  
amt_Pb209 = 0
amt_Tl209 = 0
amt_Bi209 = 0

P_Bi213_decay = 1 - 2**(-(dt/60)/46)
P_Bi213_Pb209 = P_Bi213_decay*.9791
P_Bi213_Tl209 = .0209
P_Tl209_Pb209 = 1 - 2**(-(dt/60)/2.2)
P_Pb209_Bi209 = 1- 2**(-(dt/60)/3.3)

    
cur_Bi213s, cur_Pb209s, cur_Tl209s, cur_Bi209s = [],[],[], []
for time_elapsed in range(T):
    Tl209_decays = (np.random.rand(amt_Tl209) < P_Tl209_Pb209).sum()
    Pb209_decays = (np.random.rand(amt_Pb209) < P_Pb209_Bi209).sum()
    Bi213_decays = np.random.rand(amt_Bi213) 
    
    Bi213_to_Pb209 = (Bi213_decays < P_Bi213_Pb209).sum()
    Bi213_to_Tl209 = (Bi213_decays > 1-P_Bi213_Tl209).sum()

    amt_Bi213 -= Bi213_to_Pb209+Bi213_to_Tl209
    amt_Pb209 -= Pb209_decays
    amt_Tl209 -= Tl209_decays

    amt_Bi209 += Pb209_decays
    amt_Pb209 += Tl209_decays + Bi213_to_Pb209
    amt_Tl209 += Bi213_to_Tl209
    

    cur_Bi213s.append(amt_Bi213)
    cur_Pb209s.append(amt_Pb209)
    cur_Tl209s.append(amt_Tl209)
    cur_Bi209s.append(amt_Bi209)
print(cur_Bi209s[-1],cur_Bi213s[-1],cur_Tl209s[-1],cur_Pb209s[-1])

    



