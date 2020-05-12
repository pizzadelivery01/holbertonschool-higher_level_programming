#!/usr/bin/node
// converter
exports.converter = function (base) {
  return function converts (i) {
    return i.toString(base);
  };
};
