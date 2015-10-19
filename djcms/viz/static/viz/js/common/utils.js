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

    return {
        createFactory: createFactory,
    }
});
