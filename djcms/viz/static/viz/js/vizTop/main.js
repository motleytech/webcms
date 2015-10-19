// Filename: main.js

// Require.js allows us to configure shortcut alias
// There usage will become more apparent further along in the tutorial.
require.config({
    paths: {
        jquery: '/static/js/jquery',
        d3: '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min',
        app: '/static/viz/js/vizTop/app',
        utils: '/static/viz/js/common/utils',
    }
});

define([
    // Load our app module and pass it to our definition function
    'app',
    ], function(App){
    // The "app" dependency is passed in as "App"
        var initialize = function (divId) {
            App.initialize(divId);
        };

        // What we return here will be used by other modules
        return {
          initialize: initialize,
        };
});
