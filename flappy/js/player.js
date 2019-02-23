class Player{
	constructor(x,y){
		this.x = x;
		this.y = y;
		this.velX = 0;
		this.velY = 0;
		this.size = 30;
		this.alive = true;
	}

	flap(){
		this.velY -= 4;
	}

	show(){
		noStroke();
		fill(255,255,0)
		ellipse(this.x,this.y,this.size);
	}

	update(){
		if (this.alive){
			this.velY += gravity;
			if (this.y+this.velY >= canvas.height-this.size/2){
				this.y = canvas.height-this.size/2;
				this.velY = 0;
			}
			else {
				if (this.y+this.size/2+this.velY > 0){
					this.y += this.velY;
				}
				else {
					this.y = this.size/2;
					this.velY = 0;
				}
			}

			for (var i = 0; i < pipes.length; i++){
				if (pipes[i].collided(this)){
					this.alive = false;
					panSpeed = 0;
					this.velY = 0;
				}
			}	
		}
	}
} 