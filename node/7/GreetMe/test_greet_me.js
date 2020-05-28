const assert = require("assert").strict;
var func = require("./greet_me");

let ptr = [
    // Each test pattern
    {"JACK": "Hello Jack!"},
    {"ricky": "Hello Ricky!"}
];

ptr.forEach(function(p) {
    var inp = Object.keys(p)[0];
    var exp = p[inp];

    assert.equal(func(inp), exp);
})