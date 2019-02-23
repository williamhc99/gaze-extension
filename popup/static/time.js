function checkTime(i){
	if (i < 10) {
		i = "0" + i;
	}
	return i;
}

function checkDay(h){
	if (h<12){
		return "AM";
	}
	return "PM";
}

// font-family: Quicksand;
// font-style: normal;
// font-weight: normal;
// line-height: normal;
// font-size: 130px;
function showTime(){
	document.getElementById("time").innerHTML="";

	var display = document.createElement("H1")
	var current = new Date();
	var h = current.getHours();
	var m = current.getMinutes();
	m = checkTime(m);

	var ap = checkDay(h);
	var time = document.createTextNode(h + " : " + m + " " + ap);
	display.appendChild(time);

	// append and remove
	document.getElementById("time").appendChild(display);
	// set innerHTML
	// document.body.innerHTML=h + " : " + m + " : " + s;
	setInterval(showTime, 1000);
}
showTime();