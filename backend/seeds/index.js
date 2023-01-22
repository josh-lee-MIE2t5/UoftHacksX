const mongoose = require("mongoose");
const Event = require("../models/event");

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

async function seedDb() {
  const event = new Event({
    title: "uofthacks",
    description: "hackathon",
    location: "myhal",
    _type: "competition",
    startDate: "2023-01-20",
    endDate: "2023-01-21",
    registerationReq: true,
    frequency: "yearly",
  });
  await event.save();
}

seedDb().then(() => {
  db.close();
});
