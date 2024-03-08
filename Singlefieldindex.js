db.student.createIndex({"class_id":551},
{
"createdCollectionAutomatically" :
false,
"numIndexesBefore": 1,
"numIndexsAfter": 2,
"ok" : 1
})

< class_id_551
> db.student.getIndexes()

/*Output:
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { class_id: 551 }, name: 'class_id_551' }
]*/
