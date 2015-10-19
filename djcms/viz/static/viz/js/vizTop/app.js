//Filename: app.js


define([
    'jquery',
    'd3',
    'utils',
    ],
    function($, d3, utils) {
        var App = {};

        App.init = function () {
            return this;
        };

        App.initialize = function (divId) {
            console.log("Demo App started...");
            this.divId = divId;
            console.log("Got divId : ", divId);
            this.start();
        };

        App.start = function () {
            this.addElements();
            this.createUI();
        };

        App.addElements = function () {
            $("#" + this.divId).append("<h2>My first d3 viz</h2>");
            this.d3div = $("#" + this.divId).append('<div id="d3div"></div>');
            utils.addCSSLink('/static/viz/css/vizTop/custom.css');
        };

        App.createUI = function () {
            // add d3 box, buttons and setup button callbacks.
        };

        App.getTopData = function (callback) {
            $.get("/en/api/get_top_result", "",
                    function (result) {
                        console.log("got api call result");
                        console.log(result);
                        callback();
                    }, "json");

        };

        appFactory = utils.createFactory(App);
        app = appFactory();

        // What we return here will be used by other modules
        return app;
    }
);
