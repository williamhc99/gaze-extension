class PipePair{
	constructor(order){
		this.order = order;
		this.coming = true;
		this.gap = 150;
		this.width = 50;
		this.height = floor(random(this.gap, canvas.height-this.gap));
		this.x = canvas.width + (this.order*(this.width+canvas.width)/3);
	}

	collided(p){
		if (p.x+p.size/2 > this.x && p.x-p.size < this.x + this.width) {
			if (p.y+p.size/3 > canvas.height - this.height) {
				return true;
			}
			if (p.y - p.size/3 < canvas.height - this.height - this.gap) {
				return true;
			}
		}

		if (p.x-p.size/2 > this.x + this.width && this.coming){
			this.coming = false;
			passed();
		}
		return false;
	}

	show(){
		fill(0,204,0)
		rect(this.x, canvas.height - this.height, this.width, canvas.height);
		rect(this.x, 0, this.width, canvas.height - this.height - this.gap);
	}

	update(){
		this.x -= panSpeed;
		if (this.x <= 0-this.width){
			this.height = floor(random(this.gap, canvas.height-this.gap));
			this.x = canvas.width;
			this.coming = true;
		}
	}
}