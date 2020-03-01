function select_sort(list) {
    
    for(let loop = 0; loop < list.length - 1;loop++) {
        for(let i = loop + 1; i < list.length; i++) {
            if(list[i] < list[loop]) {
                [list[loop],list[i]] = [list[i],list[loop]];
            }
        }
    }
    return list;
}

console.log(select_sort([9,6,7,8,2,3,4,5,6]))