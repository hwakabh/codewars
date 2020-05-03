const assert = require("assert").strict;
var func = require("./is_the_string_uppercase");

let params = {
    "c": false,
    "C": true,
    "hello I AM DONALD": false,
    "HELLO I AM DONALD": true,
    "ACSKLDFJSgSKLDFJSKLDFJ": false,
    "ACSKLDFJSGSKLDFJSKLDFJ": true,
};

// Parameterize Test
Object.keys(params).forEach(function(k) {
    var inp = func(k);
    var exp = params[k];

    assert.equal(inp, exp);
});
