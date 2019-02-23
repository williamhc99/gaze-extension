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

function showTime(){
	document.getElementById("time").innerHTML="";
	var d = new Date();
	// var display = document.createElement("H1");
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
	// var time = document.createTextNode(h+" : "+m+" "+ap);
	// display.appendChild(time);

	// append and remove
	// document.getElementById("time").appendChild(display);
	// set innerHTML
	document.getElementById("time").innerHTML=h+" : "+m+" "+ap;
	setInterval(showTime, 1000);
}
function showDate(){
	var d = new Date();
	var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
	var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

	document.getElementById("date").innerHTML = days[d.getDay()]+", "+months[d.getMonth()]+" "+d.getDate();

	setInterval(showDate, 60000);
}

showTime();
showDate();