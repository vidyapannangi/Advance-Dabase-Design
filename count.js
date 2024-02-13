db.trips.countDocuments();
//for counting trip duration more than 12o and subsriber
db.trips.countDocuments({tripduration: {$gt: 120}, usertype: "Subscriber"});
