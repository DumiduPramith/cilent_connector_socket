import {io_in} from 'socket.io-client'

declare var io : typeof io_in

const socket = io('127.0.0.1:8000')

socket.on('connect', ()=>{
    console.log("success connected")
})

socket.on('disconnect', ()=>{
    console.log("disconnected")
})

var list = document.getElementById("list")

socket.on("list", (data:any)=>{
    let li = ''
    for (const [key, value] of Object.entries(data)) {
        li += "<li><a href='/xterm/"+value+"'>"+key + "=" + value + "</a></li>"
    }
    list!.innerHTML = li
})
socket.emit("get_device_list",{"device": "get_device"})
setInterval(()=>{
    socket.emit("get_device_list",{"device": "get_device"})
},10000)