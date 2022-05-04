const app = require('express')();
var cors = require('cors');
const { SocketAddress } = require('net');

const httpServer = require('http').createServer(app);
app.use(cors())

const io = require('socket.io')(httpServer, {
  cors: {origin : '*'}
});

const port = process.env.PORT || 3002;
dato = ''
primo = false
links = []

io.on('connection', (socket) => {

  socket.on('login', (login) => {
    if(!primo){
      io.emit('login', '0');
      console.log('login 0' + login)
      links = login.toString().split(',')
      console.log(links)
      primo = true
    }else{
      io.emit('login', links);
      console.log('login 1' + login)
      
    }
  })



  socket.on('mosse', (mosse) => {
    dato = mosse
    console.log(dato);
    io.emit('mosse', mosse);
    //console.log(message);
    //io.emit('message', `${socket.id.substr(0, 2)} said ${message}`);
  });

  socket.on('disconnect', () => {
    console.log('a user disconnected!');
    dato = ''
    primo = false
    links = []
    io.emit('discon', 'https://i.redd.it/g4rzf4xvcn871.jpg')
  });
});

httpServer.listen(port, () => console.log(`listening on port ${port}`));