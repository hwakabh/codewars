function reverseWords(str){
  let r = str.split(' ').reverse();
  return r.join(' ');
}

module.exports = reverseWords;
