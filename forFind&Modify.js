forfind and modify
// Insert a new podcast document into the "podcasts" collection
db.podcasts.insertOne({
  title: "The Atlas Podcast",// Specify the title of the podcast
  platforms: ["Apple Podcasts", "Spotify"], // Specify the platforms where the podcast is available
  downloads: 6012, // Specify the number of downloads for the podcast
});
