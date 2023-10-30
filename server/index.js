const fs = require('fs');
const util = require('util');
const WebSocket = require("ws");

const wss = new WebSocket.Server({port: 8082});
dataBuffer = "";
currentLot = "0 0";

//const readFileContent = util.promisify(fs.readFile);
async function readFile(filePath){
  try {
    const dataBuffer = await fs.readFileSync(filePath);
  } catch (error) {
    console.error(`Got an error trying to read the file: ${error.message}`);
  }
}

// event for a new connection
wss.on("connection", ws =>{

  fs.watchFile('../Program/data.txt', (curr, prev) => {

    dataBuffer = fs.readFileSync('../Program/data.txt', 'utf8');
    const data = dataBuffer.split(" ");
//    console.log(dataBuffer);
    if (data.length = 4){
      ws.send(data[0].concat(" ", data[2]));
    }
  });

  console.log("New client connected");

  ws.on("message", data => {
    console.log(`Client has sent us: ${data}`);

    //ws.send(data.toString().toUpperCase());
  });
  ws.on("close", () => {
    console.log("Client disconnected");
  });
});
