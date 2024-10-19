const { User } = require("./models/Users");  // Correctly destructuring User from the exports

const express = require('express');
const mongoose = require('mongoose');

const app = express();

const dbConnect = async () => {
  try {
    await mongoose.connect('mongodb://127.0.0.1:27017/TableTennis');
    console.log("Successfully connected to database.");
  } catch (e) {
    console.error("Error connecting to database: ", e);
  }
};

dbConnect().catch(error => console.log(error));

app.get('/create-user', async (req, res) => {
  const newUser = new User({
    "name": "player1",
    "password": "hashed_password_123",
    "stats": {
      "totalWins": 15,
      "totalLosses": 5,
      "totalGames": 20,
      "winLossRatio": 3.0
    }
  });
  await newUser.save();
  res.send("User created");
});

app.get('/', (req, res) => {
  res.json({ user: 'geek' });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
