#!/usr/bin/node
// occurrences
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      n++;
    }
  }
  return n;
};
