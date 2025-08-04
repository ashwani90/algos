// count all chars count and compare with two strings
// sort two strings and compare them and we are done
let a = 'abcdfgerdsas';
let b = 'abcdsfgerdas';
console.log(checkAnagram(a,b))
function checkAnagram(a,b) {
    let map = {};
    for (let i=0;i<a.length;i++) {
        if (map[a[i]]) {
            map[a[i]]++;
        } else {
            map[a[i]] = 1;
        }
        
    }
    
    for (let i=0;i<b.length;i++) {
        if (map[b[i]]) {
            map[b[i]]--;
        } else {
            return false;
        }
    }
    
    for (let item in map) {
        if (map[item] !== 0) {
            return false;
        }
    }
    return true;
}
