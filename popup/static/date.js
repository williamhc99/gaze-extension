class DateDisplay(Date){
	constructor(){
		super();
		this.h = this.checkTime(super.getHours());
		this.m = this.checkTime(super.getMinutes());
		this.s = this.checkTime(super.getSeconds());


		this.str =  this.h + " : " + this.m + " : " + this.s; 
	}

	checkTime(i){
		if (i < 10) {
			i = "0" + i;
		}
		return i;
	}

	show(){
		fill(0);
		text(canvas.width/2, canvas.height/2);
	}

	update() {
		this.h = this.checkTime(super.getHours());
		this.m = this.checkTime(super.getMinutes());
		this.s = this.checkTime(super.getSeconds());


		this.str =  this.h + " : " + this.m + " : " + this.s; 
	}
}