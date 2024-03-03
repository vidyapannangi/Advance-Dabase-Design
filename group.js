db.zips.aggregate([
{
	$group:
    {
			_id: "$city", // group key
			totalZips: { $count :{ }}
		}
}
])
