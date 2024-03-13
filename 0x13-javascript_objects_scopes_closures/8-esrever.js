exports.esrever = function (list) {
  let i = list.length - 1;
  const ls = [];
  for (let j = 0; j < list.length; j++) {
    ls[j] = list[i];
    i--;
  }
  return ls;
};
