db.student.createIndex(
  { "class_id": 1 },
  {
    "name": "class_id_multikey_index",
    "createdCollectionAutomatically": false,

  }
);

< class_id_multikey_index
> db.student.getIndexes();

/* Output:
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { class_id: 'hashed' }, name: 'class_id_hashed_index' },
  { v: 2, key: { class_id: 1 }, name: 'class_id_multikey_index' }
]*/
