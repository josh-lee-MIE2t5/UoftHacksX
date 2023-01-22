const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const eventSchema = new Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  location: { type: String, required: true },
  _type: { type: String, required: true },
  startDate: { type: String, required: true },
  endDate: { type: String, required: true },
  registerationReq: { type: Boolean, required: true },
  frequency: { type: String, required: true },
});

module.exports = mongoose.model("Event", eventSchema);
