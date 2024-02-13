db.books.replaceOne(
  {_id: ObjectId("65c3ae164d257fbeae952e2d")},
  {
    _id: ObjectId("65c3ae164d257fbeae952e2d"),
    title: "Deep Dive into React Hooks",
    ISBN: "0-3182-1299-4",
    thumbnailUrl: "http://via.placeholder.com/640x360",
    publicationDate: ISODate("2022-07-28T02:20:21.000Z"),
    authors: ["Ada Lovelace"],
  }
);

db.books.replaceOne(
  {_id: ObjectId("65c3ae164d257fbeae952e2d")},
  {
    title: "Deep Dive into React Hooks",
    ISBN: "0-3182-1299-6",
    thumbnailUrl: "http://via.placeholder.com/640x360",
    publicationDate: ISODate("2022-07-28T02:20:21.000Z"),
    authors: ["Ada Lovelace"],
  }
);
//To make sure we have the doccument
db.books.findOne({_id: ObjectId("65c3ae164d257fbeae952e2d")});
