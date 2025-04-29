package kata

import "testing"

func TestCalculateYears(t *testing.T) {
	t.Run("one year", func(t *testing.T) {
		expected := [3]int{1, 15, 15}
		got := CalculateYears(1)

		if got != expected {
			t.Errorf("got: [ %q ], expected: [ %q ] \n", got, expected)
		}
	})

	t.Run("two years", func(t *testing.T) {
		expected := [3]int{2, 24, 24}
		got := CalculateYears(2)

		if got != expected {
			t.Errorf("got: [ %q ], expected: [ %q ] \n", got, expected)
		}
	})

	t.Run("ten years", func(t *testing.T) {
		expected := [3]int{10, 56, 64}
		got := CalculateYears(10)

		if got != expected {
			t.Errorf("got: [ %q ], expected: [ %q ] \n", got, expected)
		}
	})

}
