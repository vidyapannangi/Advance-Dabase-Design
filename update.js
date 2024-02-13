db.podcasts.updateOne(
  {title: "The Developer Hub"},
  {$set: {topics: ["databases", "MongoDB"]}}
);
//confirm
db.podcasts.findOne({title: "The Developer Hub"});
