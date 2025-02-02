package fizzbuzz

import (
	"fmt"
	"strings"
)

func UiFizzbuzz(maxNumber int) {
	rules := getRules()

	playGame(maxNumber, rules)

}

// getRules prompts the user for at least one rule for the game to use.
func getRules() []Rule {
	var rules []Rule = make([]Rule, 0)

	for {
		r := Rule{}
		fmt.Print("Enter a number: ")
		fmt.Scanf("%d", &r.factor)

		fmt.Print("Enter a word: ")
		fmt.Scanf("%s", &r.word)

		rules = append(rules, r)
		if !shouldContinue() {
			break
		}
	}

	return rules
}

// shouldContinue asks the user if more rules should be added.
func shouldContinue() bool {

	fmt.Print("Add another rule? [y/N] ")
	var response string
	_, err := fmt.Scanf("%s", &response)
	if err != nil {
		return false
	}
	if strings.ToLower(response) == "y" {
		return true
	}
	return false
}

// playGame plays the game with the user defined rules.
func playGame(maxNumber int, rules []Rule) {
	for number := range maxNumber {
		var found bool
		for _, rule := range rules {
			if (number+1)%rule.factor == 0 {
				found = true
				fmt.Print(rule.word)
			}
		}
		if !found {
			fmt.Print(number)
		}
		fmt.Print("\n")
	}

}
