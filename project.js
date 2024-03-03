db.zips.aggregate([
{
	$project: {
	state:1,
	zip:1,
	population:"$pop",
	_id:0
  }
}
])
