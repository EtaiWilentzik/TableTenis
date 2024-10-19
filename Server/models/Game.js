const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const User=require("./models/Users")
  //
  // {
  //   "_id": "game1",
  //   "matchId": "match1",
  //   "gameNumber": 1,
  //   "scores": {
  //     "player1": "player1",
  //     "player1Score": 21,
  //     "player2": "player2",
  //     "player2Score": 15
  //   },
  //   "datePlayed": "2024-10-12T18:30:00Z",
  //   "video": {
  //     "title": "Game 1 - Summer Open Championship",
  //     "url": "https://example.com/videos/game1.mp4",
  //     "duration": 360
  //   }
  // }

const Video = new Schema({
  title: {
      type: String
      },
  url: {
      type: String
      }
  duration: {
      type: Number
       default},
});

const Score=new Schema({
    player1:{
        type:Schema.Type.ObjectId
        ref:})
const Game=new Schema({
    gameNumber:{
        type:Number
        default:1
        },

    })
export  {Video}

