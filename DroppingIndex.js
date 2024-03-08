db.student.dropIndex({key: {student_id:551}},
{
			"createdCollectionAutomatically": false,
			"numIdexesBefore":1,
			"numIndexesAfter":2,
			"ok":1
})

/* Output:
  {
  ok: 0,
  errmsg: "can't find index with key: { key: { student_id: 551 } }",
  code: 27,
  codeName: 'IndexNotFound'
}*/
