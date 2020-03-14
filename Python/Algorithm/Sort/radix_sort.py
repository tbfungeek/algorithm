from random import randrange

def generate_test_list(start,end,count):
    return [randrange(start,end) for i in range(0,count)]

def radix_sort(list):
    print(list)

    #prepare buckets
    bucket_entries = [None] * 10
    for i in range(0,len(bucket_entries)):
        bucket_entries[i] = []

    num_digits = max_digits(list)
    #bucket sort each digit
    for digit in range(0,num_digits):

        #place into bucket
        for item in list:
            radix = get_n_digits(item,digit)
            bucket_entries[radix].append(item)

        #sort item in each bucket
        index = 0;
        for bucket_entry in bucket_entries:
            bucket_item_len = len(bucket_entry)
            if bucket_item_len == 0:
                continue
            bucket_entry[:] = sorted(bucket_entry)
            list[index:index+bucket_item_len] = bucket_entry
            index += bucket_item_len
        
        #clear bucket
        for i in range(0,len(bucket_entries)):
            bucket_entries[i] = []

def max_digits(list):
    max_item = max(list)
    return len(str(max_item))

def get_n_digits(item,n):
    str_num = str(item)
    str_len = len(str_num)
    if n >= str_len:
        return 0
    return int(str_num[str_len - 1 - n])

if __name__ == "__main__":
    test_list = generate_test_list(0,1000,10)
    radix_sort(test_list)
    print(test_list)