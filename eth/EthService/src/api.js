const express = require('express');
var app = express();
var router = express.Router();
const truffle_connect = require('./app');
var HttpStatus = require('http-status-codes');
const _ = require('lodash');
const parallel = require('async/parallel');


router.get('/accounts', (req, res) => {
    truffle_connect.start(function (result) {
        return res.status(HttpStatus.OK).send(result);
    })
});

router.post('/asset', (req, res) => {
    if (req.body.name === '' || req.body.name == undefined) {
        return res.status(HttpStatus.BAD_REQUEST).send('name is missing');
    }
    if (req.body.type === '' || req.body.type == undefined) {
        return res.status(HttpStatus.BAD_REQUEST).send('type is missing');
    }
    if (req.body.description === '' || req.body.description == undefined) {
        return res.status(HttpStatus.BAD_REQUEST).send('tdescriptionype is missing');
    }
    if (req.body.id === '' || req.body.id == undefined) {
        return res.status(HttpStatus.BAD_REQUEST).send('id is missing');
    }
    if (req.body.owner === '' || req.body.owner == undefined) {
        return res.status(HttpStatus.BAD_REQUEST).send('owner is missing');
    }
    if (req.body.address === '' || req.body.address == undefined) {
        return res.status(HttpStatus.BAD_REQUEST).send('ethereum address is missing');
    }
    truffle_connect.createAsset(req.body, (success) => {
        return res.status(HttpStatus.CREATED).send(success);
    }, (fail) => {
        return res.status(HttpStatus.INTERNAL_SERVER_ERROR).send(fail);
    });
});


router.post('/subscription/:type', async (req, res, next) => {
    let data;
    if (req.params.type === 'createAsset') {
        _.forEach(req.body.data, item => {
            data = item;
        });
        await parallel(truffle_connect.SubmitAndUpdateContext(data));
    }
    next();
    return res.status(HttpStatus.NO_CONTENT).send();
});

//expose route
app.use('/', router);

module.exports = app;

