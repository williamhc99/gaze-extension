var quotes = [ 
	"Yeet bro yeet",
	"Default",
	"Random String",
	"There's more",
	"M A C C O M M I E",
	"Fist fist fist",
	"Hey Alexa"
]

document.getElementById("quote").innerHTML = quotes[Math.floor(Math.random()*quotes.length)];
