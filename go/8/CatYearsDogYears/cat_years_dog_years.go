// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
package kata

func CalculateYears(years int) (result [3]int) {
	var ret [3]int

	if years == 1 {
		ret[0] = years
		ret[1] = 15
		ret[2] = 15
	} else if years == 2 {
		ret[0] = years
		ret[1] = 24
		ret[2] = 24
	} else {
		ret[0] = years
		ret[1] = 24 + (years-2)*4
		ret[2] = 24 + (years-2)*5
	}

	return ret
}
