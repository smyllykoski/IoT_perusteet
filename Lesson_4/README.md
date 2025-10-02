<b>Fetch</b>

<b>Overview:</b>
This project demonstrates how to fetch temperature data from a ThingSpeak channel and display it in a web browser using JavaScript.  
- Uses the **Fetch API** to request JSON data.  
- Updates the page dynamically with the received temperature information.

<b>Files:</b>
- **fetch_temp.html** &mdash; HTML page containing a header and a placeholder `<div>` for displaying temperature data.  
- **fetch_temp.js** &mdash; JavaScript file that performs the Fetch request and updates the HTML page.

<b>How it works:</b>
1. The HTML page includes a `<div id="output"></div>` to display data.  
2. The JavaScript (`fetch_temp.js`) sends a GET request to ThingSpeak to fetch the latest temperature readings.  
3. The data is processed into an array of `{time, temp}` objects and displayed as JSON in the page.  
4. Errors are logged in the browser console if the request fails.

<b>Example HTML snippet</b>
```html
<h1>Temperature Data</h1>
<div id="output"></div>
<script src="fetch_temp.js"></script>
```

<b>Example JS snippet</b>
```javascript
const url = 'https://api.thingspeak.com/channels/3079296/feeds.json?api_key=062OKCYPCLU0FYNT';

fetch(url)
  .then(response => response.json())
  .then(data => {
      const feeds = data.feeds;
      const temperatures = feeds.map(feed => ({
          time: feed.created_at,
          temp: parseFloat(feed.field1)
      }));
      document.getElementById("output").textContent = JSON.stringify(temperatures);
  })
  .catch(error => {
      console.error("Error fetching data", error);
      document.getElementById("output").textContent = "Error loading data";
  });
```
<b>How to run:</b>
1. Open `fetch_temp.html` in a modern web browser with JavaScript enabled.
2. The page will automatically fetch the latest temperature data from ThingSpeak and display it.
3. Check the browser console for any fetch errors.

---

<b>GoogleChart</b>

<b>Overview:</b>
This project demonstrates how to fetch temperature data from a ThingSpeak channel and display it as a **Google Line Chart** in a web browser.  
- Uses **Google Charts** to visualize data dynamically.  
- Fetches JSON data from ThingSpeak using the Fetch API.  

<b>Files:</b>
- **fetch_temp_chart.html** &mdash;  HTML page that loads Google Charts, fetches temperature data, and renders a line chart.  
- **fetch_temp_chart.js** &mdash;  JavaScript file that fetches temperature data and displays it as JSON (optional or for debugging).

<b>How it works:</b>
1. The HTML page includes the Google Charts loader and sets up a `<div>` to render the chart.  
2. The `drawChart` function asynchronously fetches data from ThingSpeak.  
3. Temperature readings are mapped to `[time, temperature]` pairs.  
4. The data is converted to a Google Charts `DataTable` and drawn as a LineChart.  
5. Errors are logged to the console if the fetch fails.

<b>Example HTML snippet</b>
```html
<h1>Temperature Data from Thingspeak as Google Chart</h1>
<div id="curve_chart" style="width: 900px; height: 500px"></div>
<script src="fetch_temp_chart.js"></script>
```
<b>Example JS snippet</b>
```javascript
const url = 'https://api.thingspeak.com/channels/3079296/feeds.json?api_key=062OKCYPCLU0FYNT';

fetch(url)
  .then(response => response.json())
  .then(data => {
      const feeds = data.feeds;
      const temperatures = feeds.map(feed => ({
          time: feed.created_at,
          temp: parseFloat(feed.field1)
      }));
      console.log(temperatures);
  })
  .catch(error => {
      console.error("Error fetching data", error);
  });
```
<b>How to run</b>
1. Open `fetch_temp_chart.html` in a modern web browser with JavaScript enabled.
2. The chart will automatically fetch and render the latest temperature data from ThingSpeak.
3. Open the browser console to see raw JSON data from `fetch_temp_chart.js`.

---

<b>Webhook</b>

<b>Overview:</b>
This project demonstrates how to send messages to a **Discord channel** using a webhook server built with **Node.js and Express**.  
- Receives HTTP POST requests with JSON payloads.  
- Forwards the message content to a Discord webhook URL.  
- Useful for IoT notifications, alerts, or real-time messaging.

<b>Files:</b>
- **server.js** &mdash; Node.js script that sets up the webhook server and sends messages to Discord.  
- **package.json / package-lock.json / node_modules** &mdash; Node.js dependencies.

<b>How it works:</b>
1. The server listens on port `3000` and exposes a POST endpoint `/notify`.  
2. The request must include a JSON body containing a `message` field.  
3. The server forwards this message to the specified Discord webhook URL using `fetch()`.  
4. The response confirms whether the message was successfully sent.

<b>Example POST request</b>
```bash
POST http://localhost:3000/notify
Content-Type: application/json

{
  "message": "Hello from IoT project!"
}
```
<b>Example JS snippet</b>
```javascript
app.post('/notify', (req, res) => {
    const { message } = req.body;

    if (!message) {
        return res.status(400).json({error: 'Message is required'});
    }

    fetch(DISCORD_WEBHOOK_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({content: message})
    })
    .then(response => {
        if (!response.ok) throw new Error(`Discord responded with status ${response.status}`);
        res.json({status: 'Message sent...'});
    })
    .catch(error => {
        console.error('Error sending to Discord', error);
        res.status(500).json({error: 'Failed to send your message'});
    });
});
```
<b>How to run:</b>
1. Install dependencies if not already installed:
   ```bash
   npm install
   ```
2. Start the server:
   ```bash
   node server.js
3. Send POST requests with a JSON body containing `message` to `http://localhost:3000/notify`.
4. Check your Discord channel for the received messages.

---

<b>Websocket</b>

<b>Overview:</b>
This project demonstrates real-time **bidirectional communication** between a server and a web client using **WebSockets**.  
- The server echoes back any message sent by the client.  
- Useful for IoT applications that require **instant updates** or chat-like interactions.

<b>Files:</b>
- **client.html** &mdash; Web page for sending and receiving messages via WebSocket.  
- **server2.js** &mdash; Node.js WebSocket server using the `ws` library.  
- **package.json / package-lock.json / node_modules** &mdash; Node.js dependencies.

<b>How it works:</b>
1. The **WebSocket server** listens on port `8080`.  
2. When a client connects, the server logs the connection.  
3. The client sends messages through a text input.  
4. The server echoes back each message, which is displayed in the client log.  
5. The connection closes gracefully when the client disconnects.

<b>Example JS snippet</b>
```javascript
const WebSocket = require('ws');

const server = new WebSocket.Server({ port: 8080 });

server.on('connection', socket => {
    console.log('Client connected');

    socket.on('message', message => {
        console.log('Received: ' + message.toString());
        socket.send(`Echo: ${message}`);
    });

    socket.on('close', () => {
        console.log('Client disconnected');
    });
});
```
<b>Example HTML snippet</b>
```html
<h1>WebSocket Demo</h1>
<input id="msg" />
<button onClick="sendMessage()">Send</button>
<div id="log"></div>

<script>
const socket = new WebSocket('ws://localhost:8080');

socket.onopen = () => {
    document.getElementById('log').innerText += 'Connected to server\n';
};

socket.onmessage = event => {
    document.getElementById('log').innerText += 'Server: ' + event.data + '\n';
};

function sendMessage() {
    const msg = document.getElementById('msg').value;
    socket.send(msg);
    document.getElementById('log').innerText += 'You: ' + msg + '\n';
}
</script>
```
<b>How to run:</b>
1. Install dependencies if not already installed:
   ```bash
   npm install ws
   ```
2. Start the WebSocket server:
   ```bash
   node server2.js
3. Open `client.html` in a browser.
4. Type a message and click <b>Send</b> to communicate with the server in real-time.
5. Messages are echoed back by the server and displayed in the client log.
