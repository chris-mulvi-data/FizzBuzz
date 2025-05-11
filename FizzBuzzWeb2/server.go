package main

import "fmt"
import "net/http"

func main() {
	fileServer := http.FileServer(http.Dir("./"))
	http.Handle("/", fileServer)
	if err := http.ListenAndServe(":8443", nil); err != nil {
		fmt.Println(err.Error())
	}
}
