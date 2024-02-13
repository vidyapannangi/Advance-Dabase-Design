// Insert a document into the "podcasts" collection
db.podcasts.insertOne({
  _id: ObjectId("6261a92dfee1ff300dc80bf1"),
  title: "The MongoDB Podcast",
  platforms: ["Apple Podcasts", "Spotify"],
  year: 2022,
  hosts: [],
  premium_subs: 4152,
  downloads: 2,
  podcast_type: "audio",
});
//to find
db.podcasts.findOne({title: "The MongoDB Podcast"});
db.podcasts.findOne({_id: ObjectId("6261a92dfee1ff300dc80bf1")});
