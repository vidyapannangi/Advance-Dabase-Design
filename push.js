// Update a podcast document with a specific _id to push a new platform into the 'platforms' array
db.podcasts.updateOne(
  {_id: ObjectId("6261a92dfee1ff300dc80bf1")},
  {$push: {hosts: "Nic Raboy"}}
);
// Confirmation: Retrieve and display the updated podcast document to ensure the update was successful
db.podcasts.findOne({title: "The Developer Hub"});
