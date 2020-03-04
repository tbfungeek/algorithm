function quick_search(list) {
    if(list.length < 2) return list;
    let pivot = list[0];
    let less = [];
    let greater = [];
    for(let i = 1 ;i < list.length; i++) {
        if(list[i] <= pivot) {
            less.push(list[i]);
        } else {
            greater.push(list[i]);
        }
    }
    return quick_search(less) + [pivot] + quick_search(greater);
}

console.log(quick_search([5,3,4,5,6,7,8,9,12,34,65,8,1]));