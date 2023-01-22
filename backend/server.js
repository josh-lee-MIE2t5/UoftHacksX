const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const Event = require("./models/event");
const { json } = require("express");
require("dotenv").config();

mongoose.set("strictQuery", false);

// Define the database URL to connect to.
const mongoDBurl = "mongodb://127.0.0.1:27017/eventsite";
mongoose.connect(mongoDBurl, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", () => {
  console.log("Mongo connected");
});

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.listen(port, () => {
  console.log(`Server is running on port: ${port}`);
});

app.get("/", async (req, res) => {
  const events = await Event.find({});
  res.send(events);
});

app.post("/", async (req, res) => {
  const event = new Event(req.body);
  await event.save();
  res.send(event);
});

app.get("/:_id", async (req, res) => {
  const { _id } = req.params;
  const events = await Event.find({ _id });
  res.send(events);
});

app.get("/search/:title", async (req, res) => {
  const { title } = req.params;
  const events = await Event.find({ title: { $regex: title } });
  //console.log(events);
  res.send(events);
});

app.get("/filter", (req, res) => {
  res.send("filter output endpoint");
});
