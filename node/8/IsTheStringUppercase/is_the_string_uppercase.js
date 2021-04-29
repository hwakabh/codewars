function isUpperCase(str) {
  // Paterns for uppercase string
  let ptr = /^[A-Z]+$/g;
  // Remove all except alphabets
  str = str.replace(/[^a-zA-Z]/g, '');

  return ptr.test(str);
}

module.exports = isUpperCase;