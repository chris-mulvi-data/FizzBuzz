package ui

type MenuOption struct {
	Label       string
	Description string
	Name        string
}

var MenuOptions []MenuOption = []MenuOption{
	{
		Label:       "Basic FizzBuzz",
		Description: "A very basic version with no frills.",
		Name:        "basicFizzbuzz",
	},
	{
		Label:       "Extensible FizzBuzz",
		Description: "A version of FizzBuzz that can have rules added and removed easily.",
		Name:        "extensibleFizzbuzz",
	},
}
