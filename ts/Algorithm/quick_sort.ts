function quick_sort(list:number[]) {
    if(list.length < 2) return list;
    let pivot = list[0];
    let less:number[] = [];
    let greater:number[] = [];
    for(let i = 1; i < list.length; i++) {
        if(list[i] <= pivot) {
            less.push(list[i]);
        } else {
            greater.push(list[i]);
        }
    }
    return quick_sort(less) + [pivot] + quick_sort(greater);
}   

console.log(quick_sort([1,2,3,4,8,9,23,1,23,4,5,6,78,8,23]));