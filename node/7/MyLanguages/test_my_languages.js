const assert = require("assert");
var func = require("./my_languages");

let ptr = [
    [{"Java" : 10, "Ruby" : 80, "Python" : 65}, ["Ruby", "Python"]],
    [{"Hindi" : 60, "Greek" : 71, "Dutch" : 93}, ["Dutch", "Greek", "Hindi"]],
    [{"C++" : 50, "ASM" : 10, "Haskell" : 20}, []],
];

ptr.forEach(function(p) {
    var inp = p[0];
    var exp = p[1];

    // [1, 2, 3] === [1, 2, 3] is false with strictEqual()
    assert.ok(func(inp), exp);
});