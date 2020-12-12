package main

func shiftingLetters(S string, shifts []int) string {
	str := []rune(S)
	n := len(shifts)
	for i := n - 2; i >= 0; i-- {
		shifts[i] += shifts[i + 1]
		shifts[i] %= 26
	}
	for i := 0; i < n; i++ {
		shifts[i] %= 26
		str[i] = rune((int(str[i]) - 'a' + shifts[i]) % 26 + 'a')
	}
	return string(str)
}
