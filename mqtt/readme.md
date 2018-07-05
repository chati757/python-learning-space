## install paho-mqtt for python3
    python3 -m pip install paho-mqtt

## software for testing mqtt
    mosquitto-1.4.15a-install-win32.exe (for window)
        https://mosquitto.org/download/
    
    lib requirement
        install Win32OpenSSL_light-1_0_2o 

            copy folder<installation drive>\OpenSSL-Win32\bin 
            and paste <installation drive>\mosquitto

        file<installation drive>\OpenSSL-Win32\

            libeay32.dll
            libssl32.dll
            ssleay32.dll
            *and paste <installation drive>\mosquitto
        
        
        download from : ftp://sources.redhat.com/pub/pthreads-win32/dll-latest/dll/x86/
            pthreadVC2.dll
            *and paste <installation drive>\mosquitto

## mqtt cloud setting
    https://api.cloudmqtt.com/
        
        create new instance

## mosquitto testing cmd
                         [user]     [password]          [server]          [port]    [topic]
                            |           |                   |               |          |
                            v           v                   v               v          v
        mosquitto_sub -u wuolgjlj -P 7NEws8XoqYnL -h m13.cloudmqtt.com -p 14081 -t testtopic

                         [user]     [password]          [server]          [port]     [topic]      [msg]
                            |           |                   |               |          |            |
                            v           v                   v               v          v            v
        mosquitto_pub -u wuolgjlj -P 7NEws8XoqYnL -h m13.cloudmqtt.com -p 14081 -t testtopic -m "test msg"

        *using ssl example
        mosquitto_pub.exe -u wuolgjlj -P 7NEws8XoqYnL -p 24081 -h m13.cloudmqtt.com --tls-version tlsv1.2 --cafile "<certificate dir>/addtrustexternalcaroot.crt" -t testtopic -m "test"

## using mqtt-paho 
    normal connection type
        pub_cloudmqtt_test.py
        sub_cloudmqtt_test.py
        
    ssl type
        pub_ssl_cloudmqtt_test.py
    *download certificate for cloudmqqt : https://support.comodo.com/index.php?/Default/Knowledgebase/Article/View/979/108/domain-validation-sha-2
    certificate filename : addtrustexternalcaroot.crt



    

        
    
