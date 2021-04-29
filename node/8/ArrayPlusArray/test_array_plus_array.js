const assert = require("assert").strict;
var func = require("./array_plus_array");

let ptr = [
  // Each test pattern: [inp1, inp2, exp]
  [[1, 2, 3], [4, 5, 6], 21],
  [[-1, -2, -3], [-4, -5, -6], -21],
  [[0, 0, 0], [4, 5, 6], 15],
  [[100, 200, 300], [400, 500, 600], 2100]
]

// Parameterize Test
ptr.forEach(function(p) {
  var inp = func(p[0], p[1]);
  var exp = p[2];

  assert.equal(inp, exp);
});
