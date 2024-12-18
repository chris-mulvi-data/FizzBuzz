// Package ui contains functions for interacting with the varying versions
// of FizzBuzz such as getting the number to play to and showing the version
// selection menu.
package ui

import "fmt"

func ShowMenu() {

	fmt.Println("Select a version to run.")
	for i, option := range MenuOptions {
		fmt.Printf("%d: %s\n", i, option.Label)
	}
}

func GetSelection(prompt string) int {
	var selection int
	fmt.Print(prompt)
	fmt.Scanf("%d", &selection)
	return selection
}
