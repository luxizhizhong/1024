// create by @d1y in 2019-10-05
package main

import (
	"os"
	"fmt"
	"os/exec"
)

func playURL(url) {
	exec.Command('mpv', url)
}

func main() {
	args := os.Args
	var args_len int = len(args)
	if (args_len > 1) {
		var plate string = args[1]
		fmt.Println(plate)
	} else {

	}
}