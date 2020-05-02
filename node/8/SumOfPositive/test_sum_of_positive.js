const assert = require('assert').strict;
var func = require('./sum_of_positive');

var inp = func([1, 2, 3, 4, 5]);
var exp = 15;

assert.equal(inp, exp);