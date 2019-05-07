function contains(num, arr) {
	for (var i = 0; i < arr.length; i++) {
		if (num == arr[i]) {
			return true;
		}
	}
	return false;
}

function getImage() {
	document.body.style.backgroundColor = '#000000';
	var n = Math.ceil((Math.random() * 99));
	var img = new Image()
	img.src = "https://storage.googleapis.com/gaze_pictures_test/pic" + n + ".jpg";
	document.body.style.background = "url(" + img.src + ") no-repeat center center fixed";
	document.body.style.backgroundSize = "cover";
}

getImage()

