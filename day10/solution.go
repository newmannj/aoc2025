package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func getPressResult(button string, state string) string {
	// Parse buttons
	button_list := strings.Split(strings.Trim(button, "()"), ",")
	for _, b := range button_list {
		b_index, _ := strconv.Atoi(b)
		char_at_button := string(state[b_index])
		var replace_char string
		if char_at_button == "." {
			replace_char = "#"
		} else {
			replace_char = "."
		}
		state = state[:b_index] + string(replace_char) + state[b_index+1:]

	}
	return state
}

func bfs(end_state string, cur_state string, buttons []string, last_press string, presses int) int {
	if strings.Compare(end_state, cur_state) == 0 {
		return presses
	}
	for _, b := range buttons {
		// Calculate what happens when you press button
		next_state := getPressResult(b, cur_state)
		bfs(end_state, next_state, buttons, b, presses+1)

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
	start_state := strings.Replace(strings.Clone(machine), "#", ".", -1)
	fmt.Println("getting minimal presses for machine")
	bfs(machine, start_state, buttons, "", 0)

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
