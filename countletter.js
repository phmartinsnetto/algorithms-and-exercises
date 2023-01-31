function LetterCountI(str) { 

  // code goes here 
  let wordArr = str.split(" ");
  let wordMap = {};
  let charList = [];
  let biggestCount = 0;
  let biggestWord = "";

  //looping through words
  for (let i=0; i < wordArr.length; i++) {
    //adding word to map as an object
    wordMap[wordArr[i]] = {};

    charList = wordArr[i].toLowerCase().split("");
    //looping through letters
    for (let j=0; j < charList.length; j++) {
      //checking if letter already in word object as a key
      if (wordMap[wordArr[i]].hasOwnProperty(charList[j])) {
        wordMap[wordArr[i]][charList[j]] += 1;
      } else {
        //adding letter as a key
        wordMap[wordArr[i]][charList[j]] = 1;
      }

      //check if it's bigger than actual biggest
      if (wordMap[wordArr[i]][charList[j]] > biggestCount) {
        biggestCount = wordMap[wordArr[i]][charList[j]];
        biggestWord = Object.keys(wordMap)[i];

      }
    }
  }
  if (biggestCount == 1) {
    return -1;
  }

  return biggestWord; 

}

console.log(LetterCountI("Hello apple pie"));