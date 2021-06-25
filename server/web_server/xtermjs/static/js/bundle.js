/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it uses a non-standard name for the exports (exports).
(() => {
var exports = __webpack_exports__;
/*!**********************!*\
  !*** ./src/index.ts ***!
  \**********************/

Object.defineProperty(exports, "__esModule", ({ value: true }));
const socket = io('127.0.0.1:8000');
socket.on('connect', () => {
    console.log("success connected");
});
socket.on('disconnect', () => {
    console.log("disconnected");
});
var list = document.getElementById("list");
socket.on("list", (data) => {
    let li = '';
    for (const [key, value] of Object.entries(data)) {
        li += "<li><a href='/xterm/" + value + "'>" + key + "=" + value + "</a></li>";
    }
    list.innerHTML = li;
});
socket.emit("get_device_list", { "device": "get_device" });
setInterval(() => {
    socket.emit("get_device_list", { "device": "get_device" });
}, 10000);

})();

/******/ })()
;
//# sourceMappingURL=bundle.js.map