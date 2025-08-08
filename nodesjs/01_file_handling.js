const fs=require("fs");
fs.writeFileSync("text.txt","This is a text file");
console.log("File created");

//  writeFile is Asynchronous function
//  while the writeFileSync is Synchronous function
// It means that the writeFile function will not block the execution of the next line of code
// while the writeFileSync will block the execution of the next line of code

// ./ is used if you want to create the file in the current directory
// ../ is used if you want to create the file in the parent directory

