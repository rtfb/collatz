package main

import (
	"fmt"
	"os"
	"time"
)

// collatz checks a given num for adherence to the Collatz conjecture. Returns
// the number of steps it took to reach 1.
func collatz(num int64) int {
	iters := 0
	for num != 1 {
		if num&1 == 0 {
			num = num >> 1
		} else {
			num = num + (num << 1) + 1
		}
		iters++
	}
	return iters
}

func dump(orbits []int, filename string) {
	start := time.Now()
	defer func() {
		end := time.Now()
		fmt.Printf("(writing the output took %v)\n", end.Sub(start))
	}()
	f, err := os.Create(filename)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	for i := range orbits {
		f.WriteString(fmt.Sprintf("%d: %d\n", i, orbits[i]))
	}
}

func collatzAll(count int64) {
	orbits := make([]int, count)
	orbits[0] = 0
	orbits[1] = 0
	start := time.Now()
	i := int64(2)
	for i < count {
		orbits[i] = collatz(int64(i))
		i++
	}
	end := time.Now()
	fmt.Printf("Checked first %d numbers in %v\n", count, end.Sub(start))
	dump(orbits, "orbits.txt")
}

func main() {
	count := int64(1e6)
	collatzAll(count)
}
