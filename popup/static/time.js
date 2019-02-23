function checkTime(i){
	if (i < 10) {
		i = "0" + i;
	}
	return i;
}

function checkDay(h){
	if (h<12){
		return false;
	}
	return true;
}

var d = new Date();
var id = d.getDay();

function showTime(){
	document.getElementById("time").innerHTML="";
	d = new Date();
	var h = d.getHours();
	var m = d.getMinutes();
	// var s = d.getSeconds();
	h = checkTime(h);
	m = checkTime(m);
	// s = checkTime(s);

	var ap;
	if (checkDay(h)){
		var ap = "PM";
		if (h!=12){
			h -= 12;
		}
	} else {
		var ap = "AM";
	}
	document.getElementById("time").innerHTML=h+" : "+m+" "+ap;
	setTimeout(showTime, 1000);
}

function draw(){
	document.getElementById("logo"+id).style.borderColor = "rgb(249, 255, 81)";
	document.getElementById("logo"+id).style.borderWidth = "4px";
	document.getElementById("logo"+id).style.boxShadow = "0 0 30px rgb(249, 255, 81)";
}

function showDate(){
	d = new Date();
	var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
	var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
	var id = d.getDay();

	document.getElementById("date").innerHTML = days[id]+", "+months[d.getMonth()]+" "+d.getDate();
	setTimeout(showDate, 60000);
}

showTime();
showDate();
setTimeout(draw, 600);
