const { spawn } = require("child_process");
const python = spawn("python3", ["call_from_js.py"]);


python.stdout.on("data", data => {
	console.log(data.toString());
})