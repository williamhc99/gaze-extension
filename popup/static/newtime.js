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
var h;
var m;
var ap;
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var	days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
var id;
var behind = false;

function getETHours(){
	h = d.getUTCHours()-5
	if (h<0){
		id = -1;
		behind = true;
		return h+24
	}
	id = 0;
	return h;
}

function getETDay(){
	if (behind){
		return d.getUTCDay()-1;
	}
	return d.getUTCDay();
}

function getETMonth(){
	m = d.getUTCMonth()
	if (behind){
		if (m==1 || m==3 || m==5 || m==7 || m==8 || m==10 || m==12){
			if (d.getUTCDate()==31){
				m -= 1;
			}
		} else if (m==2){
			if (d.getUTCDate()==28){
				m -= 1;
			}
		} else if (d.getUTCDate()==30){
			m -= 1;
		}
	}
	return m;
}

function getETDate(){
	if (behind){
		return d.getUTCDate()-1;
	}
	return d.getUTCDate();
}

function showTime(){
	document.getElementById("time").innerHTML="";
	h = checkTime(getETHours());
	m = checkTime(d.getUTCMinutes());

	if (checkDay(h)){
		ap = "PM";
		if (h!=12){
			h -= 12;
		}
	} else {
		ap = "AM";
	}

	document.getElementById("time").innerHTML=h+" : "+m+" "+ap;
	setInterval(showTime, 1000);
}

function showDate(){
	id = "logo"+(d.getUTCDay()+id);

	document.getElementById("date").innerHTML = days[getETDay()]+", "+months[getETMonth()]+" "+getETDate();
	document.getElementById(id).style.borderColor="rgb(255, 255, 128)";
	document.getElementById(id).style.borderWidth="5px";
	setInterval(showDate, 60000);
}

showTime();
showDate();