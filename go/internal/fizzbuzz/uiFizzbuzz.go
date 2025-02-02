package fizzbuzz

import (
	"fmt"
	"strings"
)

func UiFizzbuzz() {
	rules := getRules()

	for _, r := range rules {
		fmt.Println(r)
	}

}

// getRules prompts the user for at least one rule for the game to use.
func getRules() []Rule {
	var rules []Rule = make([]Rule, 1)

	for {
		r := Rule{}
		r.getFactor()
		r.getWord()
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
