 function rand() {
	// generate image from pic0 to pic image.length-1
 	n = Math.floor((Math.random() * 99))
 	img = "https://storage.googleapis.com/gaze_pictures/pic" + n + ".jpg"
 	return(img)
 }
 document.body.style.backgroundImage = "url(" + rand() + ")";
