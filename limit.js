db.zips.aggregate([
{

$sort: {
		pop: -1
	}
},
  {
	$limit:3
}
])
