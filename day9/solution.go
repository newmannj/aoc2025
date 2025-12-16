package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Vertex struct {
	X, Y int
}

func main() {
	// Read the input into file
	file, err := os.ReadFile("test.txt")
	if err != nil {
		log.Fatal(err)
	}
	data := string(file)
	red_tiles := map[Vertex]bool{}

	for _, v := range strings.Split(data, "\n") {
		posns := strings.Split(v, ",")
		if len(posns) == 0 {
			break
		}
		fmt.Println(v)
		posn_x, err_x := strconv.Atoi(posns[0])
		posn_y, err_y := strconv.Atoi(posns[1])
		err := errors.Join(err_x, err_y)
		if err != nil {
			log.Fatal(err)
		}
		key := Vertex{posn_x, posn_y}
		red_tiles[key] = true
	}

}
