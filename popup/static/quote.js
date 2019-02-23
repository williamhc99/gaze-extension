var quotes = [ 
	"Declutter your space today!",
	"Complete the full body scan today.",
	"Take a long walk.",
	"Observe your thoughts for fifteen minutes",
	"Define three daily goals.",
	"Be present with your family.",
	"Connect with nature!",
	"Recite positive affirmations",
	"Practice family meditation",
	"Write in a journal",
	"Set a daily intention",
	"Smile in the mirror",
	"Make your bed mindfully"
]

document.getElementById("quote").innerHTML = quotes[Math.floor(Math.random()*quotes.length)];
