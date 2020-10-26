package src

import "github.com/kataras/iris"

func GetImg(ctx iris.Context) {
	filename := ctx.Params().Get("filename")
	tagname := ctx.Params().Get("tagname")
	_ = ctx.SendFile(FilePath+tagname, filename)

}