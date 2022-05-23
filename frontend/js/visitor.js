fetch('https://fr5o002bn2.execute-api.eu-central-1.amazonaws.com/Prod/get/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('visitorCountTotal').innerText = data['visitorCount']
    })