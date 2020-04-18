from combine import *
import random
test_N=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000]# r=N/2
time_i2c_list=list([])
time_c2i_list=list([])

for i in test_N:
    sum_time_i2c=.0
    sum_time_c2i=.0
    for j in range(5):
        N=i
        r=i//2
        random_index=random.randint(0,num_combinations(N,r)-1)
        result_i2c,time_i2c=i2c_time(N,r,random_index)
        result_c2i,time_c2i=c2i_time(N,r,result_i2c)
        sum_time_i2c+=time_i2c
        sum_time_c2i+=time_c2i
    time_i2c_list.append(sum_time_i2c/3.0)
    time_c2i_list.append(sum_time_c2i/3.0)
with open('result.txt','w') as f:
    f.write('N\ti2c\tc2i\n')
    for i in range(len(test_N)):
        f.write(str(test_N[i])+'\t'+str(time_i2c_list[i])+'\t'+str(time_c2i_list[i])+'\n')
