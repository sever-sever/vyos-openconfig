
FROM alpine

# Add dependecies
RUN apk add --update python3 py3-pip \
    && pip3 install pyang==2.6.0 pyangbind==0.8.4.post1 \
    && rm -rf /var/cache/apk/*

RUN mkdir -p /opt/openconfig/yang_modules
WORKDIR /opt/openconfig

# Download and extract openconfig YANG modules
RUN wget https://github.com/openconfig/public/archive/refs/tags/v2.6.0.zip \
    && unzip v2.6.0.zip \
    && mv public-2.6.0 public \
    && rm v2.6.0.zip

RUN cp public/release/models/*.yang yang_modules/. \
    && cp -R public/release/models/*/*.yang yang_modules/. \
    && cp public/third_party/ietf/*.yang yang_modules/.

# Needs bgp replace to this, otherwise pyant cannot generate pybind bgp
# https://raw.githubusercontent.com/nanog75/code-samples/a64e8ab62844abc2b32f1a168ebbba31b35ad43d/ztp/yang/openconfig-bgp.yang

WORKDIR /opt/openconfig/yang_modules
RUN pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o oc_bgp.py openconfig-bgp.yang \
    && pyang --plugindir /usr/lib/python3.11/site-packages/pyangbind/plugin/ --format pybind -o oc_system.py openconfig-system.yang

