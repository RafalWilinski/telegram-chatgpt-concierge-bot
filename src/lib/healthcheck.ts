// Healthcheck using express server
import express from "express";

export async function healthcheck() {
  const app = express();
  const port = process.env.PORT;

  app.get("/", (req, res) => {
    res.send("ok");
  });

  console.log("Healthcheck server listening on port", port);

  app.listen(port);
}
