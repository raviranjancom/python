def count_numbers(num):
    count=1
    number=[]
    while(count<=num):
        number.append(count)
        count+=1
    return number

def count_yield(n):
    count = 1
    while(count<=n):
        yield count;
        count+=1;

n=10000000000000;
for i in count_yield(n):
    print(i)


