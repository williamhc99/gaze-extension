var panSpeed = 2;
var gravity = 0.2;
var player;
var pipe1;
var pipe2;
var pipe3;
var pipes;
var score = 0; 
var fontsize = 60;

function setup(){
	frameRate(60);
	window.canvas = createCanvas(500, 500);
	player = new Player(100,(canvas.height/2));
	pipe1 = new PipePair(0);
	pipe2 = new PipePair(1);
	pipe3 = new PipePair(2);
	pipes = [pipe1, pipe2, pipe3];

	textSize(fontsize);
}

function draw(){
	background(204, 255, 255);
	player.update();
	player.show();

	for (var i = 0; i < pipes.length; i++){
		pipes[i].update();
		pipes[i].show();
	}

	scoreDisplay();
}

function keyPressed(){

	switch(key){
		case ' ': 
			player.flap();
			break; 
	}
}

function scoreDisplay(){
	fill(255);
	text(score, canvas.width/2, 60);
}

function passed(){
	score += 1;
	for (var i=0; i<2; i++){
		pipes[i].order -=1;
	}
}