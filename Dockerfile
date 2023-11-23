
FROM alpine

# Add dependecies
RUN apk add --update python3 py3-pip nano \
    && pip3 install pyang==2.6.0 pyangbind==0.8.4.post1 \
    && rm -rf /var/cache/apk/*

RUN mkdir -p /opt/openconfig/yang_modules \
    && mkdir -p /opt/grpc
WORKDIR /opt/openconfig

# Download and extract openconfig YANG modules
RUN wget https://github.com/openconfig/public/archive/refs/tags/v2.6.0.zip \
    && unzip v2.6.0.zip \
    && mv public-2.6.0 public \
    && rm v2.6.0.zip

RUN cp public/release/models/*.yang yang_modules/. \
    && cp -R public/release/models/*/*.yang yang_modules/. \
    && cp public/third_party/ietf/*.yang yang_modules/.

# Generate bindings from YANG
WORKDIR /opt/openconfig/yang_modules
RUN pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o ../oc_bgp.py openconfig-bgp.yang \
  && pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o ../oc_system.py openconfig-system.yang \
  && pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o ../oc_network_instance.py openconfig-network-instance.yang \
  && pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o ../oc_interfaces.py openconfig-interfaces.yang \
  && pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o ../oc_local_routing.py openconfig-local-routing.yang

# Copy and bindings from YANG
# COPY scripts/generate_yang_bindings.sh .
# RUN chmod +x /opt/openconfig/yang_modules/generate_yang_bindings.sh \
#    && /opt/openconfig/yang_modules/generate_yang_bindings.sh

# gRPC
WORKDIR /opt/grpc
RUN pip3 install grpcio==1.59.3 grpcio-tools==1.59.3 \
    && wget https://github.com/sever-sever/vyos-openconfig/archive/refs/heads/main.zip -O /opt/grpc/main.zip \
    && unzip main.zip \
    && rm main.zip \
    && mv /opt/grpc/vyos-openconfig-main/grpc/* /opt/grpc/ \
    && rm -rf /opt/grpc/vyos-openconfig-main

# OpenSSL certs
RUN apk add --update openssl \
    && rm -rf /var/cache/apk/* \
    && mkdir -p /opt/certificates \
    && openssl genpkey -algorithm RSA -out /opt/certificates/server.key \
    && openssl req -new -x509 -key /opt/certificates/server.key -out /opt/certificates/server.crt -days 3650 -subj "/CN=openconfig.vyos.local"

LABEL maintainer="Viachelav Hletenko"
