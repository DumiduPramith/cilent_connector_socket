import {cmd_check} from "./cmd_checkr"
import {client} from "./get_devices"

export class DataHandler{
    private HEADER : number
    private is_cmd : boolean
    private FORMAT : string
    constructor() {
        this.HEADER = 64
        this.is_cmd = false
        this.FORMAT = "UTF-8"
    }
    receive_data(data:Buffer){
        let raw_data = data.slice(this.HEADER).toString()
        const is_cmd = cmd_check(raw_data)
        if (!is_cmd) {
            console.log('main_func',raw_data)
        }
    }
    send_data(msg: string){
        const value = this.set_header(msg)
        client.write(value)
    }

    private set_header(msg:string){
        const msg_len = msg.length
        const length = msg_len.toString()
        let new_value = length + ' '.repeat(this.HEADER-length.length-1) + "|" + msg
        return new_value
    }
}