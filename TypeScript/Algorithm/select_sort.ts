function select_sort_ts(list:number[]) {
    for(let loop:number = 0; loop < list.length -1;loop++) {
        for(let i:number = loop + 1; i < list.length; i++) {
            if(list[i] < list[loop]) {
                [list[i],list[loop]] = [list[loop],list[i]];
            }
        }
    }
    return list;
}

console.log(select_sort_ts([1,2,3,5,6,1,2,9,12,1,2,3,6]));