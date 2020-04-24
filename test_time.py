from combine import *
import random
import matplotlib.pyplot as plt
#-------测试N
test_N=[i for i in range(100,2100,100)]
r=50
time_i2c_list=list([])
time_c2i_list=list([])

for i in test_N:
    sum_time_i2c=.0
    sum_time_c2i=.0
    for j in range(10):
        N=i
        random_index=random.randint(0,num_combinations(N,r)-1)
        result_i2c,time_i2c=i2c_time(N,r,random_index)
        result_c2i,time_c2i=c2i_time(N,r,result_i2c)
        sum_time_i2c+=time_i2c
        sum_time_c2i+=time_c2i
    time_i2c_list.append(1000*sum_time_i2c/10.0)
    time_c2i_list.append(1000*sum_time_c2i/10.0)
with open('result.txt','w') as f:
    f.write('N\ti2c\tc2i\n')
    for i in range(len(test_N)):
        f.write(str(test_N[i])+'\t'+str(time_i2c_list[i])+'\t'+str(time_c2i_list[i])+'\n')

plt.plot(test_N,time_i2c_list,color='red',linewidth=3.0)
plt.tick_params(labelsize=28)
# plt.title('i2c',fontsize=26)
plt.xlabel('N',fontsize=28)
plt.ylabel('time/ms',fontsize=28)
plt.grid()
plt.show()
# plt.savefig('./i2c_N.png')

plt.plot(test_N,time_c2i_list,color='red',linewidth=3.0)
plt.tick_params(labelsize=28)
# plt.title('c2i',fontsize=28)
plt.xlabel('N',fontsize=28)
plt.ylabel('time/ms',fontsize=28)
plt.grid()
plt.show()
# plt.savefig('./c2i_N.png')

# #---------测试R  
# time_i2c_list=list([])
# time_c2i_list=list([])
# # test_R=[i for i in range(500,1000,10)]
# test_R=[1,10,100,500,1000]
# N=2000

# for r in test_R:
#     sum_time_i2c=.0
#     sum_time_c2i=.0
#     for j in range(10):
#         index=num_combinations(N,r)-1
#         result_i2c,time_i2c=i2c_time(N,r,index)
#         result_c2i,time_c2i=c2i_time(N,r,result_i2c)
#         sum_time_i2c+=time_i2c
#         sum_time_c2i+=time_c2i
#     time_i2c_list.append(1000*sum_time_i2c/10.0)
#     time_c2i_list.append(1000*sum_time_c2i/10.0)

# with open('result_R.txt','w') as f:
#     f.write('R\ti2c\tc2i\n')
#     for i in range(len(test_R)):
#         f.write(str(test_R[i])+'\t'+str(time_i2c_list[i])+'\t'+str(time_c2i_list[i])+'\n')
        
# plt.plot(test_R,time_i2c_list)
# plt.tick_params(labelsize=20)
# plt.title('i2c',fontsize=20)
# plt.xlabel('R',fontsize=20)
# plt.ylabel('time/ms',fontsize=20)
# plt.show()
# # plt.savefig('./i2c_R.png')

# plt.plot(test_R,time_c2i_list)
# plt.tick_params(labelsize=20)
# plt.title('c2i',fontsize=20)
# plt.xlabel('R',fontsize=20)
# plt.ylabel('time/ms',fontsize=20)
# plt.show()
# # plt.savefig('./c2i_R.png')