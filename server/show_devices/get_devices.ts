import {DataHandler} from './data_handler'
import {Socket, createServer} from 'net'

export const client = new Socket()

const server = createServer((c)=>{
    console.log("client connected")
    c.on('end', ()=>{
        console.log("client disconnected")
    })
})
server.listen({host: 'localhost', port: 3000})

const data_handler = new DataHandler()
client.connect({port:5050, host:'127.0.1.1'})
client.on('data', (data) => {
    data_handler.receive_data(data)
})

setInterval(()=>{
    data_handler.send_data('__GET_DEVICES__')
}, 5000)