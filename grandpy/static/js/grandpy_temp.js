

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

function random_question(min, max) {
	const sentence1 = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?<br />";
	const sentence2 = "Cet endroit a une histoire particulière. En voici un extrait:<br />";
	const sentence3 = "Ah oui, une petite anecdote concernant ce lieu:<br />";
	const sentence4 = "Tu sais, il y a une histoire très intéressante concernant ce quartier:<br />";
	const sentence5 = "Je ne voudrais pas me la raconter mais j'en connais un petit bout sur ce quartier:<br />";
	var sentence_array = [sentence1, sentence2, sentence3, sentence4, sentence5];
	min = Math.ceil(1);
	max = Math.floor(5);
	let number = Math.floor(Math.random() * (max - min +1)) + min;
	let random_sentence = sentence_array[number];
	document.querySelector("#box1 p").innerHTML += "<p class='robotresponse'>" + random_sentence + "</p>";
}

//Main script
document.getElementById("mySearch").focus();
var form = document.querySelector("form");
form.addEventListener("submit", function(e) {
	e.preventDefault();
	let formData = form.elements.mySearch.value;
	
	const p = document.createElement('p');
	let pParent = document.getElementById("box1");
	pParent.appendChild(p);
	document.querySelector("#box1 p").setAttribute("class", "bloc1");
	document.querySelector("#box1 p").innerHTML += "<p class='question'>" + formData + "</p>"; 
	start_animate();
	
	//Using xmlhttprequest with Ajax to push a request
	var xhr = new XMLHttpRequest();	
	xhr.open('POST', '/processing/');
	xhr.addEventListener('readystatechange', function() {
		if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
			stop_animate();
			document.querySelector("#box1 p").innerHTML += "<p class='robotresponse'>Bien sûr mon ami, je connais son adresse! La voici :</p>";
			var searched_address = JSON.parse(xhr.responseText);
			var address = searched_address.data.address;
			var description = searched_address.data.description;
			document.querySelector("#box1 p").innerHTML += "<p class='address'>" + address + "</p>";
			const url = "https://www.google.com/maps/embed/v1/place?";
			var re = / /gi;
			var q = address;
			q = q.replace(re, '+');
			document.querySelector("#box1 p").innerHTML +=
				"<iframe src=" + url + "key=" + key + "&q=" + q +
				" name='myFrame' id='myFrame'></iframe><br />";
			// Adding random sentence : 
			random_question(1, 5);
			document.querySelector("#box1 p").innerHTML += "<p class='robotresponse' align='left'>" + description + "</p>";
			document.querySelector("#box1 p").innerHTML += "<hr>";
		}
		else if (xhr.status !== 200 && xhr.readyState === XMLHttpRequest.DONE) {
			stop_animate();
			document.querySelector("#box1 p").innerHTML +=
				"<p class='robotresponse'>Désolé mon ami mais je n'ai pas trouvé de réponse à ta recherche.</p>";
			document.querySelector("#box1 p").innerHTML += "<hr>";
		}
	});
	
	//Sending question to Google API
	var myform = new FormData();
	myform.append('mySearch', formData);
	xhr.send(myform)
	form.elements.mySearch.value = "";
	document.getElementById("mySearch").focus();
});			
