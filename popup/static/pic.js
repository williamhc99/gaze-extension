 const badPics = [275,118,365,30,161, 28, 120, 326, 393, 48, 32, 0, 24 ,12, 26, 11, 78, 264, 149, 8, 305, 249, 330, 134, 289, 390, 90, 367, 272, 312, 210, 278, 373, 142, 201, 311, 320, 227, 211, 71, 207, 243, 327, 65, 228, 340, 375, 234, 110, 222, 51, 206, 103, 133]
 function contains(num, arr){ 
	console.log(num) 
    for (var i = 0; i < arr.length; i++){
		if (num == arr[i]){
			return true;
		}
	}
	return false;
}
 
 function rand() {
	var n;
	do{
		n = Math.floor((Math.random() * 400));
	} while (contains(n, badPics))
	img = "https://storage.googleapis.com/gaze_pictures/pic" + n + ".jpg";
	return(img);
 }
 document.body.style.backgroundImage = "url(" + rand() + ")";
