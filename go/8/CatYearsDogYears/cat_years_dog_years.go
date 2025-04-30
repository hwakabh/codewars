// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
package kata

func CalculateYears(years int) (result [3]int) {
	var r [3]int

	if years == 1 {
		r[0] = years
		r[1] = 15
		r[2] = 15
	} else if years == 2 {
		r[0] = years
		r[1] = 24
		r[2] = 24
	} else {
		r[0] = years
		r[1] = 24 + (years-2)*4
		r[2] = 24 + (years-2)*5
	}

	return r
}
