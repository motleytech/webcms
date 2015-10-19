//Filename: app.js


define([
    'jquery',
    'utils',
    ],
    function($, utils) {
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
            $.get("/en/api/get_top_result", "",
                    function (result) {
                        console.log("got api call result");
                        console.log(result);
                    }, "json");
        }

        appFactory = utils.createFactory(App);
        app = appFactory();

        // What we return here will be used by other modules
        return app;
    }
);
