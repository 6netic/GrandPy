

function start_animate() {
	var imgAnimate = new Image();
	imgAnimate.src = "../static/img/loading.gif"; 
	let animate = document.getElementById("animation");
	animate.appendChild(imgAnimate);
}


function stop_animate() {
	let animate = document.getElementById("animation");
	animate.innerHTML = ("");
}

function random_question() {
	const sentence1 = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?<br />";
	const sentence2 = "Cet endroit a une histoire particulière. En voici un extrait:<br />";
	const sentence3 = "Ah oui, une petite anecdote concernant ce lieu:<br />";
	const sentence4 = "Tu sais, il y a une histoire très intéressante concernant ce quartier:<br />";
	const sentence5 = "Je ne voudrais pas me la raconter mais j'en connais un petit bout sur ce quartier:<br />";
	var sentence_array = [sentence1, sentence2, sentence3, sentence4, sentence5];
	var number = Math.floor(Math.random() * 5) + 1;
	var random_sentence = sentence_array[number];
	document.getElementById("box1").innerHTML += random_sentence;
}


//Main script
document.getElementById("mySearch").focus();
var form = document.querySelector("form");
form.addEventListener("submit", function(e) {
	e.preventDefault();
	let formData = form.elements.mySearch.value;
	document.getElementById("box1").innerHTML += formData + "<br />";
	start_animate();
	//Using Ajax to push a request
	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/processing/');
	xhr.addEventListener('readystatechange', function() {
		if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
			stop_animate();
			document.getElementById("box1").innerHTML += "Bien sûr mon ami, je connais son adresse! La voici : <br />";
			var searched_address = JSON.parse(xhr.responseText);
			address = searched_address.data.address;
			description = searched_address.data.description;
			document.getElementById("box1").innerHTML += '<span>' + address + '</span><br />';
			
			const url = "https://www.google.com/maps/embed/v1/place?";
			var re = / /gi;
			var q = address;
			q = q.replace(re, '+');
			document.getElementById("box1").innerHTML += 
				"<p><iframe width='450' height='250' frameborder='0' src=" + 
				url + "key=" + key + "&q=" + q +
				" name='myFrame' id='myFrame'></iframe></p>";

			// Adding random sentence : 
			random_question();
			document.getElementById("box1").innerHTML += "<p>" + description + "</p>";
		}
		else if (xhr.status !== 200 && xhr.readyState === XMLHttpRequest.DONE) {
			stop_animate();
			document.getElementById("box1").innerHTML += 
				"<p>Désolé mon ami mais je n'ai pas trouvé de réponse à ta recherche</p>";
		}
	});
	
	//Sending question to Google API
	var myform = new FormData();
	myform.append('mySearch', formData);
	xhr.send(myform)
	form.elements.mySearch.value = "";
	document.getElementById("mySearch").focus();
});			
