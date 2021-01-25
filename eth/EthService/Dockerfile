# use latest version of node
# service is under development
FROM node:10

# set working directory
WORKDIR /EthService

#copy package json
COPY package*.json ./

#installing dependencies
RUN npm install

#install truffle globally
RUN npm install -g truffle@4.1.15

# bundle source code
COPY . .

# compile contract
RUN npm run compile

# expose port 3002
EXPOSE 3002

# start app with npm
CMD ["npm", "start"]
