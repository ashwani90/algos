const string = "waterbottle";
const subString = "erbottlewat";
let isRotation = false;
let newString = string;
let tempString = "";
if (string==subString) {
    isRotation = true;
}
for (let i=0;i<string.length;i++) {
    tempString += string[i];
    newString = newString.replace(string[i], "");
    if (subString == newString+tempString) {
        isRotation = true;
    }
    
}

console.log(isRotation);