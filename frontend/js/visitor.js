fetch('https://c8bhagdr6l.execute-api.eu-central-1.amazonaws.com/PROD/put')
/*    .then(() => fetch('https://c8bhagdr6l.execute-api.eu-central-1.amazonaws.com/PROD/get'))*/
    .then(response => response.json())
    .then(data => {
        document.getElementById('visitorCount').innerText = data['visitorCount']
    })