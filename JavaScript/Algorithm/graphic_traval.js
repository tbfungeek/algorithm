function graphic_traval(grahic,start,end) {
    let search_queue = new Array();
    let searched = new Array();
    search_queue.push(...grahic[start]);
    while(search_queue.length > 0) {
        let target = search_queue.shift();
        if(searched.indexOf(target) >=0) {
            continue;
        }
        if(target === end) {
            return searched;
        }
        search_queue.push(...grahic[target]);
        searched.push(target);
    }
    return searched;
}

let graphic = {}
graphic["O"] = ["A","B"]
graphic["A"] = ["C"]
graphic["B"] = ["D","E"]
graphic["C"] = ["F"]
graphic["D"] = ["C"]
graphic["E"] = ["C"]
graphic["F"] = []

console.log(graphic_traval(graphic,"O","F"))