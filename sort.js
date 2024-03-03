db.zips.aggregate([
{
$sort: {
		pop: -1
	}
}
])
