db.zips.aggregate([
{
	$project: {
	state:1,
	zip:1,
	population:"$pop",
	pop_2022: { $round: { $multiply: [1.0031, "$pop"]}},
	_id:0
}
}
])
