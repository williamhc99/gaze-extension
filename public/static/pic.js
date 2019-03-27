//  const badPics = [238, 187, 139, 46, 202, 144, 143, 80, 252, 349, 275,118,365,30,161, 28, 120, 326, 393, 48, 32, 0, 24 ,12, 26, 11, 78, 264, 149, 8, 305, 249, 330, 134, 289, 390, 90, 367, 272, 312, 210, 278, 373, 142, 201, 311, 320, 227, 211, 71, 207, 243, 327, 65, 228, 340, 375, 234, 235, 110, 222, 51, 206, 103, 133]
 function contains(num, arr){ 
    for (var i = 0; i < arr.length; i++){
		if (num == arr[i]){
			return true;
		}
	}
	return false;
}

 
 function img() {
	 var n = Math.ceil((Math.random() * 81));
	var img = new Image()
	img.src = "https://storage.googleapis.com/gaze_pictures_test/pic" + n + ".jpg";
	return(img.src);
 }
 document.body.style.background = "url(" + img() + ") no-repeat center center fixed";

//  document.body.html.backgroundSize = "cover";
//  document.body.html.backgroundRepeat = "no-repeat";
//  document.body..position = "center center";
