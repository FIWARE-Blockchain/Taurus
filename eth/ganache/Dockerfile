FROM node:10

# expose to the 8545 port
ENV PORT 8545

# installing the dependencies 
RUN npm install -g --unsafe-perm ganache-cli && \
    npm install -g truffle && \
    npm set progress=false

EXPOSE 8545
# start the testrpc
CMD ganache-cli --hostname=0.0.0.0 -m 'route harbor drastic pigeon asset circle vintage robust catalog vendor okay vault'