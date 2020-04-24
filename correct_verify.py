from combine import *
import random
test_N=[9,12]
for N in test_N:
    random_index=random.randint(0,num_combinations(N,4)-1)
    result_i2c,time_i2c=i2c_time(N,4,random_index)
    result_c2i,time_c2i=c2i_time(N,4,result_i2c)
    print('n=',N,'r=4','index=',random_index,'combination=',result_i2c)
    print('n=',N,'r=4','combination=',result_i2c,'index=',result_c2i)