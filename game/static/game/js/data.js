const data = [];

for (const array_exercises of exercise) {
  const engPhrase = array_exercises[1];
  const spaPhrase = array_exercises[2];
  const phraseByWord = [];

  for (const word of words) {
    if (word[word.length - 1] === array_exercises[0]) {
      phraseByWord.push({
        word: word[0],
        trans: word[1],
        highlighted: word[2],
      });
    }
  }

  data.push({
    engPhrase: engPhrase,
    spaPhrase: spaPhrase,
    phraseByWord: phraseByWord,
  });
}

console.log(data);
