playing = true


// generate empty cave
var cave = [];
for (let i = 0, line ; i < h ; i++, cave.push(line)) {
    line = [];
    for (let j = 0; (j < w); j++) {
        line.push(null);
    }
}
console.log(cave);
var coordinates = [0, 0];
cave[0][0] = 'Player';

function randint(max) {        //excludes max
    return Math.floor(Math.random() * max);
}

function leftright(index) {
    if (index < 0) {
        return w -2 - index;
    } else if (index >= w) {
        return index - w;
    } else {
        return index;
    }
}

function updown(index) {
    if (index < 0) {
        return h - 2 - index;
    } else if (index >= h) {
        return index - h;
    } else {
        return index;
    }
}

function adjacent(x, y) {
    return [cave[updown(y-1)][x],       //above
            cave[updown(y+1)][x],       //below
            cave[y][leftright(x-1)],    //left
            cave[y][leftright(x+1)]];   //right
}

function placing(item) {
    var x, y
    do {
        x = randint(w);
        y = randint(h);
        console.log(x, y, item);
    } while (adjacent(x, y).includes("Player") || cave[y][x] !== null);
    cave[y][x] = item;
}
// randomise location
placing('Pit');
placing('Pit');      //2 pits
placing('Wumpus');
placing('Gold');
console.log(cave);


function move(direction) {
    if (direction === 'left') {
        coordinates[0] = leftright(coordinates[0] - 1);
    } else if (direction === 'up') {
        coordinates[1] = updown(coordinates[1] - 1);
    } else if (direction === 'down') {
        coordinates[1] = updown(coordinates[1] + 1);
    } else if (direction === 'right') {
        coordinates[0] = leftright(coordinates[0] + 1);
    }
    console.log(coordinates);
    let location = cave[coordinates[1]][coordinates[0]];

    //css
    $(".curr_room").removeClass("curr_room");
    var room = $("#"+ coordinates[0] + "-" + coordinates[1]);
    room.empty();
    room.addClass("curr_room");

    //surroundings
    var adj = adjacent(coordinates[0], coordinates[1])
    //win lose and adjacency check
    if (location === 'Pit') {                               //pit lose
        room.append("<i data-feather='x-circle'></i>");
        end('lose');
    } else if (location === 'Wumpus') {                        //wumpus lose
        room.append("<i data-feather='frown'></i>");
        end('lose');
    } else if (location === 'Gold') {                        //gold win
        room.append("<i data-feather='award'></i>");
        end('win');
    } else if (adj.includes('Pit')) {                       //pit warning
        room.append("<i data-feather='wind'></i>");
    } else if (adj.includes('Wumpus')) {                       //wampus warning
        room.append("<i data-feather='alert-triangle'></i>");
    } else if (adj.includes('Gold')) {                       //gold warning
        room.append("<i data-feather='star'></i>");
    }

    feather.replace(); // replace data-feather attribute with corresponding icon
}


function end(result) {              //result = 'win' or 'lose'
    $('.' + result).show("fast");
    playing = false;
}


$(document).ready(function(){
    //html arrow buttons
    $('#left').click(() => {move('left');});
    $('#right').click(() => {move('right');});
    $('#up').click(() => {move('up');});
    $('#down').click(() => {move('down');});
    // detecting arrow keys
    $(document).keydown(function(key) {
        if (key.keyCode == 37) {            //left
            move('left');
        } else if (key.keyCode == 38) {     //up
            move('up');
        } else if (key.keyCode == 39) {     //right
            move('right');
        } else if (key.keyCode == 40) {     //down
            move('down');
        }
    })
})
