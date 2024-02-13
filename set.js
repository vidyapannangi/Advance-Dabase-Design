//to find
db.podcasts.findOne({title: "The MongoDB Podcast"});
db.podcasts.findOne({_id: ObjectId("6261a92dfee1ff300dc80bf1")});

//to set array
db.podcasts.updateOne({_id: ObjectId("6261a92dfee1ff300dc80bf1")},{$set:{subscribers:98562}})
