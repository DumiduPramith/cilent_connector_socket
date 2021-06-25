"use strict";
exports.__esModule = true;
var socket = io('127.0.0.1:8000');
socket.on('connect', function () {
    console.log("success connected");
});
socket.on('disconnect', function () {
    console.log("disconnected");
});
