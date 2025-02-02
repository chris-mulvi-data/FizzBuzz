package fizzbuzz

import "testing"

func Test_playGame(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		maxNumber int
		rules     []Rule
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			playGame(tt.maxNumber, tt.rules)
		})
	}
}
