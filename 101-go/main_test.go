package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCollatz(t *testing.T) {
	tests := []struct {
		input int
		want  int
	}{
		{5, 5},
		{12, 9}, // 12, 6, 3, 10, 5, 16, 8, 4, 2, 1 = 9 steps, excluding the initial 12
		{11, 14},
		{16, 4},
		{1 << 17, 17},
		{1 << 59, 59},
	}
	for _, test := range tests {
		got := collatz(int64(test.input))
		assert.Equal(t, test.want, got)
	}
}
