cd /crypto/Misc/blind-xor/                                    && ncat -ve "/bin/cat flag.txt"  -lk 10098 &

cd /crypto/Asymmetric/RSA/easy-baby-RSA/                      && ncat -ve "/bin/cat server.py" -lk 10051 &
cd /crypto/Asymmetric/RSA/factor-attack/                      && ncat -ve "/bin/cat server.py" -lk 10056 &
cd /crypto/Asymmetric/RSA/factor-attack2/                     && ncat -ve "/bin/cat server.py" -lk 10057 &
cd /crypto/Asymmetric/RSA/common-modulus/                     && ncat -ve "/bin/cat server.py" -lk 10060 &
cd /crypto/Asymmetric/RSA/hastad-broadcast/                   && ncat -ve "/bin/cat server.py" -lk 10063 &
cd /crypto/Asymmetric/RSA/wiener-attack/                      && ncat -ve "/bin/cat server.py" -lk 10066 &
cd /crypto/Asymmetric/chinese-remainder/modular-sqrt/         && ncat -ve "/bin/cat server.py" -lk 10073 &
cd /crypto/Asymmetric/chinese-remainder/pohlig-hellman/       && ncat -ve "/usr/local/bin/python server.py" -lk 10077 &
# cd /crypto/Asymmetric/chinese-remainder/pohlig-hellman2/      && ncat -ve "/usr/local/bin/python server.py" -lk 10078 &
cd /crypto/Asymmetric/chinese-remainder/discrete-logarithm/   && ncat -ve "/bin/cat server.py" -lk 10080 &

cd /crypto/Symmetric/Feistel-Cipher/Xtea-Baby/                && ncat -ve "/usr/local/bin/python server.py" -lk 10003 &
cd /crypto/Symmetric/Feistel-Cipher/DES-checkbits/            && ncat -ve "/usr/local/bin/python server.py" -lk 10005 &
cd /crypto/Symmetric/ECB-mode/cut-paste/                      && ncat -ve "/usr/local/bin/python server.py" -lk 10008 &
cd /crypto/Symmetric/ECB-mode/prepend-oracle/                 && ncat -ve "/usr/local/bin/python server.py" -lk 10009 &
cd /crypto/Symmetric/CBC-mode/bit-flipping/                   && ncat -ve "/usr/local/bin/python server.py" -lk 10011 &
cd /crypto/Symmetric/CBC-mode/CBC-MAC/                        && ncat -ve "/usr/local/bin/python server.py" -lk 10014 &
cd /crypto/Symmetric/CBC-mode/padding-oracle/                 && ncat -ve "/usr/local/bin/python server.py" -lk 10018 &
cd /crypto/Symmetric/Stream-Cipher/RC4/                       && ncat -ve "/usr/local/bin/python server.py" -lk 10024 &
cd /crypto/Symmetric/Stream-Cipher/LFSR/                      && ncat -ve "/usr/local/bin/python server.py" -lk 10026 &
cd /crypto/Symmetric/Stream-Cipher/XORShift/                  && ncat -ve "/usr/local/bin/python server.py" -lk 10028 &
cd /crypto/Symmetric/OFB-mode/useful-nonce/                   && ncat -ve "/usr/local/bin/python server.py" -lk 10031 &
cd /crypto/Symmetric/CFB-mode/secret-game/                    && ncat -ve "/usr/local/bin/python server.py" -lk 10034 &
cd /crypto/Symmetric/CTR-mode/useful-nonce2/                  && ncat -ve "/usr/local/bin/python server.py" -lk 10036 &
cd /crypto/Symmetric/GCM-mode/forbidden-attack/               && ncat -ve "/usr/local/bin/python server.py" -lk 10039 &
cd /crypto/Symmetric/HashLEA/mao192/                          && ncat -ve "/usr/local/bin/python server.py" -lk 10042 &
cd /crypto/Symmetric/HashClash/md5clash/                      && ncat -ve "/usr/local/bin/python server.py" -lk 10045 &
cd /crypto/Symmetric/HashLEA/cookie/                          && /usr/local/bin/python manage.py runserver 0.0.0.0:10049