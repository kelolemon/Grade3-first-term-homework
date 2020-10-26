package src

import (
	"github.com/kataras/iris"
	"io/ioutil"
)

func GetFileList(ctx iris.Context) {
	TagName := ctx.FormValue("tag")
	files, _ := ioutil.ReadDir(FilePath + TagName + "/")
	DataList := FileList {
		List: make([]FileInfo, 0),
	}
	for _, f := range files {
		DataFile := FileInfo {
			FileName: f.Name(),
			FileSize: f.Size(),
		}
		DataList.List = append(DataList.List, DataFile)
	}
	_, _ = ctx.JSON(DataList)
}
