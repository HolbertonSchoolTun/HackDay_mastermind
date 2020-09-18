#!/usr/bin/node

const chalk = require('chalk');
const boxen = require('boxen');

const welcome = chalk.white.bold('Lets play a game... A MASTERMIND GAME ')
const boxenOptions = {
    padding: 1,
    margin: 1,
    borderStyle: "round",
    borderColor: "green"
};

const welcomeMessage = boxen(welcome, boxenOptions);

let black = 0;
let white = 0;
const baseColors = ['r', 'g', 'b', 'y', 'o', 'p'];
let secret = []
for (let i=0; i < 4; i++) {
    let rand = Math.floor(Math.random() * baseColors.length);
    secret.push(baseColors[rand]);
}
copy = secret;
function black_count(a, b, c, d){
    if (a === secret[0]) {
        black += 1;
    }
    if (b === secret[1]) {
        black += 1;
    }
    if (c === secret[2]) {
        black += 1;
    }
    if (d === secret[3]) {
        black += 1;
    }
    return black;
}

function white_count(a, b, c, d, blck){
    if (secret.includes(a)) {
        white += 1;
    }
    if (secret.includes(b)) {
        white += 1;
    }
    if (secret.includes(c)) {
        white += 1;
    }
    if (secret.includes(d)) {
        white += 1;
    }
    return white - black;
}

function playerVsBot(a, b, c, d) {
    blck = black_count(a, b, c, d);
    w = white_count(a, b, c, d, blck);
    return {'black': blck, 'white': w};
}
const colors = require('colors');
my_str = "";
console.log(welcomeMessage);
console.log('  Usage: abcd for each color a significant letter:'.cyan);
console.log('\t\t### r: Red'.red);
console.log('\t\t### g: Green'.green);
console.log('\t\t### b: Blue'.blue);
console.log('\t\t### y: Yellow'.bgYellow.black);
console.log('\t\t### o Orange'.yellow);
console.log('\t\t### p: Purple'.magenta);

console.log('\x1b[36m%s\x1b[0m', '\t    GUESS MY COMBINATION !!');

console.log(secret);

const prompt = require('prompt-sync')();
for (let i=0; i < 10 && black < 4; i++) {
    const input = prompt('');
    my_str = input;
    if (!my_str) {
        break;
    }
    time_left = 9 - i;
    console.log(playerVsBot(my_str[0], my_str[1], my_str[2], my_str[3]));
    if (black === 4) {
        console.log('Congratulations you\'re a MasterMind'.red);
        break;   
    }
    if (my_str === "surrender" || i === 9) {
        console.log(secret);
        console.log('Better luck next time!!'.cyan);
        break;
    }
    console.log('#'.cyan + time_left + ` Tries To Go`);
    black = 0;
    white = 0;
}
