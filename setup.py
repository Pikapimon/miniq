import os
os.system('apt-get install shadowsocks-libev')
with open('/etc/shadowsocks-libev/config.json', 'w') as f:
    f.write('{\
    "server": "0.0.0.0", \
    "mode": "tcp_and_udp", \
    "server_port": 2230, \
    "local_port": 1080, \
    "password": "k9J3E6H2eBA3", \
    "timeout": 60, \
    "method": "chacha20-ietf-poly1305" \
}')

os.system('/etc/init.d/shadowsocks-libev restart')
