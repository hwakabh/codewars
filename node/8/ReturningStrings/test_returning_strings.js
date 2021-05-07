const assert = require('assert').strict;
let func = require('./returning_strings');

let ptr = [
  {"Ryan": "Hello, Ryan how are you doing today?"},
  {"Shingles": "Hello, Shingles how are you doing today?"}
];

ptr.forEach(function(p) {
  let inp = Object.keys(p)[0];
  let exp = p[inp];

  assert.equal(func(inp), exp);
})
