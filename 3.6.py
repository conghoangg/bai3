print("NGUYỄN CÔNG HOÀNG")
print("MSSV:235752021610013")

def get_sum(*num): 
 tmp = 0 
 # duyet cac tham so 
 for i in num: 
  tmp += i 
 return tmp 
result = get_sum(1, 2, 3, 4, 5) 
print(result) 