package main

import (
	"bufio"
	"fmt"
	"os/exec"
	"strings"
)

var (
	js = "./joystick-json"
)

func main() {
	cmd := exec.Command(js)
	cmdReader, _ := cmd.StdoutPipe()
	scanner := bufio.NewScanner(cmdReader)
	done := make(chan bool)
	go func() {
		for scanner.Scan() {
			temp := strings.Split(scanner.Text(), `\n`)
			fmt.Println(temp)

		}
		done <- true
	}()
	cmd.Start()
	<-done
	cmd.Wait()
}
