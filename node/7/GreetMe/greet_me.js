var greet = function(name) {
  // Convert all chars to lowercase
  let l = name.toLowerCase();
  // Select first char and make it uppercase, and concatinate to get rest of the chars
  let cap_name = l.charAt(0).toUpperCase() + l.slice(1);
  return `Hello ${cap_name}!`;
};

module.exports = greet;
