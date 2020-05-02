const assert = require('assert').strict;
var func = require('./multiply');

// Set parameters for unit-testings
var inp = func(1, 2);
var exp = 2;

// Check expected and actual
// - If codes run as expected, no stdout will be shown.
// - If codes have some bugs, AssertionError will be raised.
assert.equal(inp, exp);
