/*
utility methods
*/

define([], function () {
    var createFactory = function (proto) {
        /*
        factory creation util method. Makes object creation easier.
        Prefer composition in place of inheritance.
        */
        const factory = function () {
            const obj = Object.create(proto);
            return obj.init.apply(obj, arguments);
        };
        factory.proto = proto;
        return factory;
    };

    var addCSSLink = function (url) {
        var link = document.createElement('link');
        link.setAttribute('rel', 'stylesheet');
        link.setAttribute('type', 'text/css');
        link.setAttribute('href', url);
        document.getElementsByTagName('head')[0].appendChild(link);
    }

    return {
        createFactory: createFactory,
        addCSSLink: addCSSLink,
    }
});
