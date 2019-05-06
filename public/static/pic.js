function contains(num, arr) {
	for (var i = 0; i < arr.length; i++) {
		if (num == arr[i]) {
			return true;
		}
	}
	return false;
}


function img() {
	var n = Math.ceil((Math.random() * 81));
	var img = new Image()
	img.src = "https://storage.googleapis.com/gaze_pictures_test/pic" + n + ".jpg";
	return (img.src);
}
document.body.style.background = "url(" + img() + ") no-repeat center center fixed";
document.body.style.backgroundSize = "cover";
