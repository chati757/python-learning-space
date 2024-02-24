import time

count = 0
result = []
n_init = 0
def generate_numbers(total, n, current_list):
    global count
    global result
    global n_init 
    if(n_init==0):
        n_init = n
    if n == 1:
        current_list.append(total)
        result.append(current_list)
    else:
        for i in range(int(total * 101), -1, -1):
            new_total = round(total - (i / 100.0),2)
            if new_total >= 0:
                generate_numbers(new_total, n - 1, current_list + [i / 100.0])
    
    if(len(result) >= 1000000 or current_list==[]):
        print(len(result))
        print(n_init)
        result = []

if __name__=='__main__':
    start_time = time.time()
    generate_numbers(1, 5, [])
    end_time = time.time()
    print(f"{end_time - start_time:.4f} sec")

    #print(result)
    print(len(result))
    print(result[:5])
    print(result[-5:])
