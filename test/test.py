from tools import *

print('validating correctness:')
#* each batch tests one array with size = n , and t from 1 to sum(array)
batches=10
#* size of the array
n=10
correctness_validation(batches,n)



 
#* n from 2 to max_n
max_n=10
#* t from 1 to max_t
max_t=500
#* 
distribution=randint
#* parameter of distribution
var=10

z=time_rec(max_n,max_t,var,distribution)

#record data
record_data(z,max_n,max_t,var,distribution)

