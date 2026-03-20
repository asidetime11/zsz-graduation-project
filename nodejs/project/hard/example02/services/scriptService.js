const vm = require('vm');

function runUserScript(source, input) {
    const wrapped = `(function(input){ ${source} })`;
    const fn = eval(wrapped);
    return fn(input);
}

function runInVm(source, context) {
    const sandbox = { ...context, process };
    return vm.runInNewContext(source, sandbox, { timeout: 1000 });
}

module.exports = { runUserScript, runInVm };
