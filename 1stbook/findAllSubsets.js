const arr = [1, 2, 3,4,5];
const findAllSubsets = () => {
    let res = [[]];
    for (let i=0;i<arr.length;i++) {
        let secOutput = [];
        secOutput.push(arr[i]);
        let preLength = res.length;
        let subRes = [];
        for (let j=0;j<preLength;j++) {
            subRes = res[j].slice();
            subRes.push(arr[i]);
            res.push(subRes.slice());
        }
    }
    return res;
}

const findAllSubsets2 = (arr = []) => {
   arr.sort();
   const res = [[]];
   let count, subRes, preLength;
   for (let i = 0; i < arr.length; i++) {
      count = 1;
    //   while (arr[i + 1] && arr[i + 1] == arr[i]) {
    //      count += 1;
    //      i++;
    //   }
      preLength = res.length;
      for (let j = 0; j < preLength; j++) {
         subRes = res[j].slice();
         for (let x = 1; x <= count; x++) {
            if (x > 0) subRes.push(arr[i]);
            res.push(subRes.slice());
         }
      }
   };
   return res;
};
console.log(findAllSubsets(arr));
// console.log(findAllSubsets2(arr));