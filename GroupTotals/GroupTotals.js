function GroupTotals(strArr) { 

    // code goes here 
    let inputMap = {};
    let tempKey = "";
    let tempValue = "";
    let tempStr = "";
    let joinArr = [];
    let string = "";
  
    //transform parameter in Object/map
    //also cleans key duplicates
    for (let i = 0; i < strArr.length; i++) {
      //split in the :
      tempKey = strArr[i].split(":")[0];
      tempValue = Number(strArr[i].split(":")[1]);
  
      if(!(inputMap.hasOwnProperty(tempKey))) {
        inputMap[tempKey] = 0;
      }
      inputMap[tempKey] += tempValue;
    }
  
    //deleting the keys with 0 as value
    for (prop in inputMap) {
      if (inputMap[prop] == 0) {
        delete inputMap[prop];
      }
    }
  
    //transform into strings array
    for (prop in inputMap) {
      tempStr = prop + ":" + inputMap[prop].toString();
      joinArr.push(tempStr);
    }
  
    //order elements
    joinArr.sort();
    //join with ,
    string = joinArr.join(",");
  
    return string; 
  
  }

  console.log(GroupTotals(["X:-1", "Y:1", "X:-4", "B:3", "X:5"]));
