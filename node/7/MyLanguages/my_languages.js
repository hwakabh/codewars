function myLanguages(results) {
  let ans = Object.keys(results).filter(function(k) {
    return results[k] >= 60;
  }).sort(function(a, b) {
    return results[b] - results[a];
  })
  
  return ans;
}

module.exports = myLanguages;
