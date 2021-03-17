var snake = [];/* [x, y, direction] */
var snake_length = 3;
var snake_dire = [];
var table = [];
for(i = 0; i < 75; i++){
    table.push([]);
    for(j = 0; j < 170; j++){
        table[i].push(0);
    }
}
var timestamp = 100;
var init_x, init_y, point_x, point_y;
var direction;//0.up 1.right 2.down 3.left
let CanMove = true;

function Snake(body){
    var bool = Array.isArray(body[0]);
    if(bool){
        Snake(body[0]);
        Snake(body.slice(1, body.length));
    }else{
        x = body[0];
        y = body[1];
        dire = body[2];
        $("#" + y + "-" + x).css("background-color", "white");
    }
}

function eat(){
    snake_length += 1;
    snake_dire.push(snake_dire[snake_dire.length - 1]);
    $("#Snake_length").val(snake_length);
    var tmp = [snake[snake.length - 1][0], snake[snake.length - 1][1], snake_dire[snake_dire.length - 1]];
    snake.push(tmp);
    while(true){
        point_x = Math.floor(Math.random() * 170);
        point_y = Math.floor(Math.random() * 75);
        if(table[point_y][point_x] == 0){
            $("#" + point_y + "-" + point_x).css("background-color", "red");
            table[point_y][point_x] = 2;
            break;
        }
    }
}

function Draw(){
    $("td#" + snake[snake.length - 1][1] + "-" + snake[snake.length - 1][0]).css("background-color", "black");
    table[snake[snake.length - 1][1]][snake[snake.length - 1][0]] = 0;
    
    for(i = snake.length - 1; i > 0; i--){
        snake[i] = snake[i - 1].slice();
    }
    if(snake[0][2] == 0){
        snake[0][1] -= 1;
    }else if(snake[0][2] == 1){
        snake[0][0] += 1;
    }else if(snake[0][2] == 2){
        snake[0][1] += 1;
    }else if(snake[0][2] == 3){
        snake[0][0] -= 1;
    }
    if((snake[0][0] < 0 || snake[0][0] > 169) || (snake[0][1] < 0 || snake[0][1] > 74) || table[snake[0][1]][snake[0][0]] == 1){
        alert("Failed");
        timestamp = 0;
        return;
    }else if(table[snake[0][1]][snake[0][0]] == 2){
        eat();
        table[snake[0][1]][snake[0][0]] = 1;
    }
    Snake(snake);
    $("#init_x").val(init_x);
    $("#init_y").val(init_y);
    CanMove = true;
}

$(document).ready(function(){
    init_x = Math.floor(Math.random() * (166 - 3 + 1)) + 3;
    init_y = Math.floor(Math.random() * (71 - 3 + 1)) + 3;
    if(Math.abs(init_x - 0) < Math.abs(init_x - 170)){
        direction = 1;
    }else if(Math.abs(init_x - 0) > Math.abs(init_x - 170)){
        direction = 3;
    }else{
        direction = Math.floor(Math.random() * 4);
    }
    $("#Init_x").val(init_x);
    $("#Init_y").val(init_y);
    $("#Direction").val(direction);
    $("#Snake_length").val(snake_length);
    for(i = 0; i < snake_length; i++){
        var tmp = [init_x, init_y, direction];
        snake.push(tmp);
        if(direction == 0){
            init_y += 1;
        }else if(direction == 1){
            init_x -= 1;
        }else if(direction == 2){
            init_y -= 1;
        }else if(direction == 3){
            init_x += 1;
        }
    }
    Snake(snake);
});

$(document).ready(function(){
    while(true){
        point_x = Math.floor(Math.random() * 170);
        point_y = Math.floor(Math.random() * 75);
        if(table[point_y][point_x] == 0){
            $("#" + point_y + "-" + point_x).css("background-color", "red");
            table[point_y][point_x] = 2;
            break;
        }
    }
});

window.setInterval(Draw, timestamp);

window.addEventListener('keydown', function(e){
    if(CanMove){
        CanMove = false;
        if(snake[0][2] != 2 && e.code == "ArrowUp"){
            snake[0][2] = 0;
        }else if(snake[0][2] != 3 && e.code == "ArrowRight"){
            snake[0][2] = 1;
        }else if(snake[0][2] != 0 && e.code == "ArrowDown"){
            snake[0][2] = 2;
        }else if(snake[0][2] != 1 && e.code == "ArrowLeft"){
            snake[0][2] = 3;
        }else if(e.code == "Space"){
            snake_length += 1;
            snake_dire.push(snake_dire[snake_dire.length - 1]);
            $("#Snake_length").val(snake_length);
            var tmp = [snake[snake.length - 1][0], snake[snake.length - 1][1], snake_dire[snake_dire.length - 1]];
            snake.push(tmp);
        }
        $("#Direction").val(snake[0][2]);
    }
});