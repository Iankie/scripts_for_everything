fetch('http://<TARGET-ENDPOINT>', {
	method: 'POST',
	mode: 'same-origin',
	credentials: 'same-origin',
	headers: {
		// change content-type if you need
		'Content-Type':'application/x-www-form-urlencoded'
	},

body:'<POST-DATA>'
})
