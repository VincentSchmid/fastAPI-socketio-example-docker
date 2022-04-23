# fastAPI_socketio_test
server-client containers communicating using socketio docker-compose included

running the docker-compose will put the two containers in the same network. Client is exposed over 8081.

Exposed API:  
#### GET localhost:8081/connect  
This connects the client to the server.  
  
#### GET localhost:8081/send/{message}  
Message will be printed to server console.  
