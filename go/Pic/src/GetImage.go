package src

import "github.com/kataras/iris"

func GetImg(ctx iris.Context) {
	filename := ctx.URLParamDefault("filename", "")
	tagname := ctx.URLParamDefault("tagname", "")
	_ = ctx.SendFile(FilePath + tagname + "/" + filename, filename)

}