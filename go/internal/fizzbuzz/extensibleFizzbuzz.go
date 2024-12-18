package fizzbuzz

import "fmt"

type rule struct {
	factor int
	word   string
}

// A list of rules for the game. Adding or removing rules has no
// impact on the functionality of the game.
var rules []rule = []rule{
	{3, "Fizz"},
	{5, "Buzz"},
	{7, "Bazz"},
}

func ExtensibleFizzBuzz(maxNumber int) {
	for i := range maxNumber {
		i++
		play(i)
	}
}

func play(number int) {
	found := false
	for _, rule := range rules {
		if number%rule.factor == 0 {
			found = true
			fmt.Print(rule.word)
		}
	}
	if !found {
		fmt.Print(number)
	}
	fmt.Print("\n")
}
