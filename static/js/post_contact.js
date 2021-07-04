const form = document.getElementById('submitButton')
form.addEventListener('click', (e) => {
    e.preventDefault()
    const name = document.querySelector('#name').value
    const email = document.querySelector('#email').value
    const phone = document.querySelector('#phone').value
    const message = document.querySelector('#message').value

    const data = {
        name,
        email,
        phone,
        message
    }

    console.log(data);


    const url = 'http://127.0.0.1:5000/json'
    fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then(response => response.text())

        // Displaying results to console
        .then(json => console.log(json));

})



// Converting to JSON
