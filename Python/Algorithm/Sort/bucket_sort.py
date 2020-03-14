
def bucket_sort(list,bucket_num):
    if list is None or len(list) < 2 or bucket_num <= 0:
        return

    print(list)

    bucket_entries = [None]*bucket_num

    #prepare bucket struct
    for i in range(0,bucket_num):
        bucket_entries[i] = []

    #prepare bucket gap value
    min_item = min(list)
    max_item = max(list)
    bucket_gap = (max_item - min_item) / (bucket_num - 1)

    #store item in bucket
    for item in list:
        bucket_index = int((item - min_item)/bucket_gap)
        bucket_entries[bucket_index].append(item)
        print("{} {}".format(bucket_index,item))

    print(bucket_entries)

    #sort each bucket and get result
    index = 0
    for bucket_entry in bucket_entries:
        bucket_entry[:] = sorted(bucket_entry)
        bucket_item_len = len(bucket_entry)
        list[index:index+bucket_item_len] = bucket_entry
        index += bucket_item_len

if __name__ == '__main__':

    test_list = [4.12,6.421,0.0023,3.0,2.123,8.122,4.12,10.09,11,88,45,0.001]
    bucket_sort(test_list,4)
    print(test_list)
    