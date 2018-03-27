function permutate(str){
// debugger
    if (str.length < 2) return str;

    let permutations = [];

    for (var i = 0; i < str.length; i++) {
    
        let item = str[i];
        // if (str.indexOf(item) != i) continue; // THAT LINE *OR* LINE 2 OF THE FOR LOOP BELOW
        // IMPORTANT LINE
        let strWoCurrChar = str.substr(0, i) + str.substr(i+1, str.length); 
        for ( let subStr of permutate(strWoCurrChar) ){
            let temp = item + subStr;
            if (permutations.indexOf(temp) >= 0) break;  // skip if a permutation is have been inserted
            permutations.push(temp);
        }
    }

    return permutations;

}