const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const userStats = new Schema({
  totalWins: { type: Number, default: 0 },
  totalLosses: { type: Number, default: 0 },
  totalGames: { type: Number, default: 0 },
  winLossRatio: { type: Number, default: 0 }
});

const userSchema = new mongoose.Schema({
  name: {
      type: String,
      required: true
  },
  password: {
      type: String,
      required: true
  },
  stats: userStats
});

const User = mongoose.model('User', userSchema);
module.exports = { User };
