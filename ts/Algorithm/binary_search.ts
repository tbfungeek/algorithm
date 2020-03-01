function binary_search(list:number[],target:number) {
    if(list.length == 0) return -1;
    let hight:number = list.length;
    let low:number   = 0;

    while (low <= hight) {
        let mid_index:number = ~~((hight + low)/2);
        //js 取整方式 ~~number  number^0  number<<0
        let mid_value:number = list[mid_index];
        
        if(target < mid_value) {
            hight = mid_index - 1;
        } else if(target > mid_value) {
            low = mid_index + 1;
        } else {
            return mid_index;
        }
    }
    return -1;
}

console.log(binary_search([1,2,3,4,5,6,7,12],4))

