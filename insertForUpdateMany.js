db.books.insertMany([
  {
    _id: 17,
    title: "MongoDB in Action",
    isbn: "1935182870",
    pageCount: 0,
    publishedDate: ISODate("2011-12-12T08:00:00.000Z"),
    thumbnailUrl:
      "https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/banker.jpg",
    shortDescription: "MongoDB In Action is a comprehensive guide to MongoDB",
    longDescription:
      "MongoDB is a document-oriented database that's highly scalable and delivers very high-performance",
    status: "LEGACY",
    authors: ["Kyle Banker"],
    categories: ["Next Generation Databases"],
    instock: false,
  },
  {
    _id: 18,
    title: "Node.js in Action",
    isbn: "1617292575",
    pageCount: 0,
    publishedDate: ISODate("2013-10-15T08:00:00.000Z"),
    thumbnailUrl: "https://example.com/nodejs.jpg",
    shortDescription: "Node.js in Action is a comprehensive guide to Node.js",
    longDescription:
      "Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.",
    status: "LEGACY",
    authors: [
      "Mike Cantelon",
      "Marc Harter",
      "TJ Holowaychuk",
      "Nathan Rajlich",
    ],
    categories: ["Web Development", "Node.js"],
    instock: false,
  },
  {
    _id: 19,
    title: "Learning React",
    isbn: "1491954620",
    pageCount: 0,
    publishedDate: ISODate("2017-04-27T08:00:00.000Z"),
    thumbnailUrl: "https://example.com/react.jpg",
    shortDescription: "Learning React is a comprehensive guide to React",
    longDescription:
      "React is a JavaScript library for building user interfaces.",
    status: "LEGACY",
    authors: ["Alex Banks", "Eve Porcello"],
    categories: ["Web Development", "React"],
    instock: false,
  },
]);
