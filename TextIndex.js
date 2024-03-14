db.student.createIndex(
  { "class_id": "text" },
  {
    "name": "class_id_text_index",
    "default_language": "english", // Set the default language if needed

  }
);

< class_id_text_index
> db.student.getIndexes();

/* Output:
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { class_id: 'hashed' }, name: 'class_id_hashed_index' },
  { v: 2, key: { class_id: 1 }, name: 'class_id_multikey_index' },
  {
    v: 2,
    key: { _fts: 'text', _ftsx: 1 },
    name: 'class_id_text_index',
    weights: { class_id: 1 },
    default_language: 'english',
    language_override: 'language',
    textIndexVersion: 3
  }
]*/
