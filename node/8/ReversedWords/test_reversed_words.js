const assert = require('assert').strict;
let func = require('./reversed_words');

let ptr = [
  {"hello world!": "world! hello"},
  {"yoda doesn't speak like this": "this like speak doesn't yoda"},
  {"foobar": "foobar"},
  {"kata editor": "editor kata"},
  {"row row row your boat": "boat your row row row"}
];

ptr.forEach(function(p) {
  let inp = Object.keys(p)[0];
  let exp = p[inp];

  assert.equal(func(inp), exp);
});
