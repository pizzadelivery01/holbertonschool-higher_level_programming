#!/usr/bin/node
// js print argv

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
