const app = require('express')();

const PORT = 7777;

app.listen(
	PORT,
	() => console.log(`it's alive on http://localhost:${PORT}`)
)
