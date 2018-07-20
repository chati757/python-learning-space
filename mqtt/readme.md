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

## mqtt cloud setting (aws)
    register > https://aws.amazon.com/th/iot/

    Services > IoT Core > Manage > Thing > Create > Create a single thing > enter name > create type > select type > create group > add group > next > One-click certificate creation (recommended) 
    download certificate for this thing , private key , root ca > Activate > Attach a policy > select policy (if not create policy first) > register thing

## create user (cli) to generate credential for work with websocket port 443 (aws)
    aws website (logged in) > security , identity & compliance > IAM
        add user
            Users > add user
            [checked] Programmatic access
            next until complete > save 

        add group
            Groups > Create New Group > check <name group>
            tab Permissions > Attach Policy > AWSIoTFullAccess > Attach Policy
            tab Users > Add Users to Group > <username form add user>

    set environment for use credential
        window (command prompt)
            set AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
            set AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
            set AWS_DEFAULT_REGION=us-west-2

        linux , macOs or Unix
            $ export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
            $ export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
            $ export AWS_DEFAULT_REGION=us-west-2
        
        or set filepath in ..Python35\Lib\site-packages\AWSIoTPythonSDK\core\protocol\connection\cores.py
        line at : 132 : self._credentialConfigFilePath = "~/.aws/credentials" or "<your credential path>"
        
        create credential file
            ~/.aws/credentials or ~/.aws/config
                [default]
                aws_access_key_id=AKIAIOSFODNN7EXAMPLE
                aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
                region=us-west-2
                output=json
        
    
    run script aws_sdk_pub_sub_tls_socket_awsmqtt_test.py

## modify aws paho library for support ssl wrapsocket at port 8883 (aws)
    ..\Python35\Lib\site-packages\AWSIoTPythonSDK\core\protocol\paho\client.py
        atline 816
            else:
                if self._port == 8883:
                    self._ssl = ssl.wrap_socket(
                    sock,
                    certfile=self._tls_certfile,
                    keyfile=self._tls_keyfile,
                    ca_certs=self._tls_ca_certs,
                    cert_reqs=self._tls_cert_reqs,
                    ssl_version=self._tls_version,
                    ciphers=self._tls_ciphers)
                else:
                    context = ssl.SSLContext(self._tls_version)
                    context.load_cert_chain(self._tls_certfile, self._tls_keyfile)
                    context.verify_mode = self._tls_cert_reqs
                    context.load_verify_locations(self._tls_ca_certs)
                    context.set_alpn_protocols(["x-amzn-mqtt-ca"])
            
                    self._ssl = context.wrap_socket(sock, server_hostname=self._host, do_handshake_on_connect=False)
                    
                    self._ssl.do_handshake()
                
                if self._tls_insecure is False:
                    if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 5):  # No IP host match before 3.5.x
                        self._tls_match_hostname()

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

## using mqtt-paho (cloudmqtt)
    normal connection type
        pub_cloudmqtt_test.py
        sub_cloudmqtt_test.py
        
    ssl type
        pub_ssl_cloudmqtt_test.py
    *download certificate for cloudmqqt : https://support.comodo.com/index.php?/Default/Knowledgebase/Article/View/979/108/domain-validation-sha-2
    certificate filename : addtrustexternalcaroot.crt