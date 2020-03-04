function binary_search(list,item) {

    if(!list.length) return -1;

    let hight = list.length;
    let low   = 0;

    while(low <= hight) {
        let middle = parseInt((hight + low) / 2);
        let midValue = list[middle];
        if(item < midValue) {
            hight = middle - 1;
        } else if(item > midValue) {
            low   = middle + 1;
        } else {
            return middle;
        }
    }

    return -1;
}

console.log(binary_search([],9));