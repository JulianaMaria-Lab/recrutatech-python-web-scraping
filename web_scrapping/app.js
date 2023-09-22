const express = require("express")

const app = express()

app.get("/", function(req, res){
    res.sendFile(__dirname + "/src/index.html");
});

app.listen(8000);

console.log("Rodando na porta 8000")