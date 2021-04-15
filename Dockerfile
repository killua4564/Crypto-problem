FROM    python:3.7.9-alpine3.12

RUN     apk update
RUN     apk add nmap-ncat gcc libc-dev gmp-dev mpfr-dev mpc1-dev
RUN     pip install --upgrade pip setuptools
RUN     pip install Django gmpy gmpy2 owiener pycryptodome sympy tqdm xortool
RUN     pip install msgpack==0.6.0 

WORKDIR         /crypto
COPY            . .
ENTRYPOINT      sh /crypto/entrypoint.sh
