package main

import (
	"fmt"
	"math"
)

func longestPalindrome(s string) string {
	if len(s) == 0 {
		return ""
	}
	str := make([]rune, 0)
	str = append(str, '$')
	str = append(str, '#')
	for i := 0; i < len(s); i++ {
		str = append(str, rune(s[i]))
		str = append(str, '#')
	}
	p := make([]int, len(str))
	center := 0
	boundary := 0
	maxAns := 0
	maxPos := 0
	for i := 1; i < len(str); i++ {
		p[i] = 1
		if boundary > i {
			p[i] = int(math.Min(float64(boundary - i), float64(p[2 * center - boundary])))
		}
		for i - p[i] >= 0 && i + p[i] < len(str) && str[i - p[i]] == str[i + p[i]] {
			p[i]++
		}
		if p[i] + i > boundary {
			boundary = p[i] + i - 1
			center = i
		}
		if p[i] - 1 > maxAns {
			maxAns = p[i] - 1
			maxPos = i
		}
	}
	ans := make([]rune, 0)
	for i := maxPos - maxAns; i < maxPos + maxAns; i++ {
		if str[i] != '#' {
			ans = append(ans, str[i])
		}
	}
	return string(ans)
}

func main() {
	s := "aacabdkacaa"
	fmt.Println(longestPalindrome(s))
}