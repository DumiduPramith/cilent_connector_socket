import { show_devices } from "./cmd_func"

export function cmd_check(raw_data:string){
    if (raw_data.startsWith('__')){
        let data = raw_data.split('|')
        switch (data[0]){
            case '__DEVICE_LIST__':
                show_devices(data[1])
                return true
            default:
                return false

        }
    }
}