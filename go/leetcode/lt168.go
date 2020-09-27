package main

func convertToTitle(n int) string {
	if n == 0 {
		return ""
	}
	return convertToTitle((n-1)/26) + string(rune((n-1)%26+65))
}

