package fizzbuzz

import "fmt"

type Rule struct {
	factor int
	word   string
}

// get the factor to be used from a user
func (r Rule) getFactor() {
	fmt.Print("Enter a number: ")
	fmt.Scanf("%d", &r.factor)
}

func (r Rule) getWord() {
	fmt.Printf("Enter a word: ")
	fmt.Scanf("%s", &r.word)
}
