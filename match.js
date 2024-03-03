db.zips.aggregate([
    {
      $group: {
        _id: "$state",
        total_pop: { $sum: "$pop" }
      }
    },
    {
      $match: {
        total_pop: { $lt: 1000000 }
      }
    }
])
