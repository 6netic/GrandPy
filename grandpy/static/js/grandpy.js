/* Custom JS file for grandpy app */

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

document.querySelector(".form-group #mySearch").focus();
var form = document.querySelector("form");

/* Submitting search sentence */
form.addEventListener("submit", function(e) {
	e.preventDefault();
	let dataFromForm = form.elements.mySearch.value;
	const p = document.createElement('p');
	var pParent = document.getElementById("box1");
	var paragraph = pParent.appendChild(p);
	paragraph.setAttribute("class", "bloc1");
	paragraph.innerHTML += "<p class='question'>" + dataFromForm + "</p>";
	start_animate();
	form.elements.mySearch.value = "";
	document.querySelector(".form-group #mySearch").focus();
	var myform = new FormData();
	myform.append('mySearch', dataFromForm);
	
	fetch("/processing/", {
				method: "POST",
  				body: myform
	})
		.then(
			function(response) {
				if(response.status !== 200) {
					stop_animate();
					paragraph.innerHTML += 
					"<p class='robotresponse'>Désolé mon ami mais je n'ai pas trouvé de réponse à ta recherche.</p>";
				}
				// Response is ok - extracting data
				response.json().then(function(data) {
					stop_animate();
					paragraph.innerHTML += 
						"<p class='robotresponse'>Bien sûr mon ami, je connais son adresse! La voici :</p>";
					paragraph.innerHTML += 
						"<p class='address'>" + data.data.address + "</p>";
					
					//Inserting the map of that place					
					const url = "https://www.google.com/maps/embed/v1/place?";
					let re = / /gi;
					let q = data.data.address;
					q = q.replace(re, '+');
					paragraph.innerHTML += 
						"<iframe src=" + url + "key=" + key + "&q=" + q +
						" name='myFrame' id='myFrame'></iframe><br />";
					
					// Adding random sentence function: 
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
						paragraph.innerHTML += "<p class='robotresponse'>" + random_sentence + "</p>";
					}
					random_question(1, 5);
					paragraph.innerHTML += 
						"<p class='robotresponse' align='left'>" + data.data.description + "</p>";
				}); 
			}		
		)
});


