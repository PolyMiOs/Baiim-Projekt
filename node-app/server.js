const http2 = require("http2");
const fs = require("fs");
const path = require("path");

const poemContent = fs.readFileSync(path.join(__dirname, "poem.txt"), "utf8");
const poemLines = poemContent.split("\n");

const server = http2.createSecureServer({
  key: fs.readFileSync("server.key"),
  cert: fs.readFileSync("server.crt"),
  maxSessionMemory: 100,
});

// prevent server crashing with error catching
server.on("error", (err) => console.error("Server Error:", err));
server.on("sessionError", (err) => console.error("Session Error:", err));

server.on("stream", (stream, headers) => {
  const urlPath = headers[":path"];
  const method = headers[":method"];
  if (urlPath === "/search" && method === "POST") {
    let body = "";
    stream.on("data", (chunk) => {
      body += chunk;
    });
    stream.on("end", () => {
      const start = Date.now();
      let matches = [];
      let errorMsg = "";

      try {
        // create a Regex object from user input
        const userRegex = new RegExp(body, "i");

        // use the regex to filter the lines
        matches = poemLines.filter((line) => userRegex.test(line));
      } catch (e) {
        errorMsg = "Invalid Regular Expression.";
      }

      const duration = Date.now() - start;

      let html = `
        <html>
        <body style="font-family:sans-serif; background:#1a1a1a; color:#0f0; padding:20px;">
          <h1>Regex Search Results for: <code style="color:white;">${body}</code></h1>
          <p style="color:yellow;">Processing time: ${duration}ms</p>
          <hr>
          ${errorMsg ? `<p style="color:red;">${errorMsg}</p>` : ""}
          ${matches.length > 0 ? `<ul>${matches.map((l) => `<li>${l}</li>`).join("")}</ul>` : "<p>No matches found.</p>"}
          <br><a href="/" style="color:white;">Back to Poem</a>
        </body>
        </html>`;

      if (!stream.destroyed) {
        stream.respond({ ":status": 200, "content-type": "text/html" });
        stream.end(html);
      }
    });
  } else {
    // Simulate a slow database query or something - takes 1s
    setTimeout(() => {
      try {
        stream.respond({
          ":status": 200,
          "content-type": "text/plain; charset=utf-8",
        });
        stream.end(poemContent);
      } catch (e) {}
    }, 1000);
  }
});
server.listen(443, () => {
  console.log("Server is up. Try to crash me.");
});
