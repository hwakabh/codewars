function arrayPlusArray(arr1, arr2) {
  var sum = 0;
  arr1.forEach(function(i) {
    sum += i;
  });
  arr2.forEach(function(j) {
    sum += j;
  });
  return sum;
}

module.exports = arrayPlusArray;
