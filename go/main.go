package main

import (
	"chirs-mulvi-data/fizzbuzz/internal/fizzbuzz"
	"chirs-mulvi-data/fizzbuzz/internal/ui"
	"fmt"
)

var maxNumber int = 30

func main() {
	ui.ShowMenu()
	selection := ui.GetSelection("Select one: ")
	if selection > len(ui.MenuOptions)-1 {
		return
	}
	fmt.Println(ui.MenuOptions[selection].Description)
	switch ui.MenuOptions[selection].Name {
	case "basicFizzbuzz":
		fizzbuzz.BasicFizzBuzz(maxNumber)
	case "extensibleFizzbuzz":
		fizzbuzz.ExtensibleFizzBuzz(maxNumber)
	case "uiFizzbuzz":
		fizzbuzz.UiFizzbuzz(maxNumber)
	}
}
