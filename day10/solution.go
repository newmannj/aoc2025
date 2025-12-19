package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func bfs(end_state string, cur_state string, buttons []string, last_press string, presses int) int {
	if strings.Compare(end_state, cur_state) == 0 {
		return presses
	}
	// Otherwise, press all buttons except for the one that was pressed
	// to get into this state.
	return 0

}

func getMinimalPresses(line string) int {
	var machine string
	var buttons []string
	splitLine := strings.Split(line, " ")
	machine = strings.Trim(splitLine[0], "[]")
	buttons = splitLine[1 : len(splitLine)-1]
	fmt.Println(machine)
	fmt.Println(buttons)

	return 0
}

func main() {
	file, err := os.Open("test.txt")
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		getMinimalPresses(scanner.Text())
	}

}
