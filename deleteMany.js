//for finding many birds
db.birds.find({conservationStatus:"Least Concern"})
//deleting many
db.birds.deleteMany({conservationStatus:"Least Concern"})
