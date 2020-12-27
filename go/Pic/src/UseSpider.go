package src

import (
	"fmt"
	"github.com/kataras/iris"
	"log"
	"os/exec"
)

func UseSpider(ctx iris.Context) {
	TagName := ctx.FormValue("tagname")
	go func (tag string) {
		cmd := exec.Command("./spider", tag)
		out, err := cmd.CombinedOutput()
		if err != nil {
			log.Fatalf("cmd.Run() failed with %s\n", err)
		}
		fmt.Printf("combined out:\n%s\n", string(out))
	}(TagName)
	RtData := RtMsg{
		Code: 0,
		Msg: "Begin to spider",
	}
	_, _ = ctx.JSON(RtData)
}
