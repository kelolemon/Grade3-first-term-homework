package main

import "fmt"


func test() func() int {
	i := 1
	return func() int {
		i++
		return i
	}
}

func main() {
	f := test()
	fmt.Println(f(), f(), f(), f())
}