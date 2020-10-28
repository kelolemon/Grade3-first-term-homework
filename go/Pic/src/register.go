package src

import (
	"context"
	"github.com/kataras/iris"
	"go.mongodb.org/mongo-driver/bson"
)

const FilePath = "./img/"
const URLPath = "/img/"

func Register(ctx iris.Context) {
	// get info
	Name := ctx.FormValue("username")
	Pass := ctx.FormValue("password")
	// get img
	// create User info
	UserData := User {
		Username: Name,
		Password: Pass,
	}
	var result User
	collection := Client.Database("Pic").Collection("UserInfo")

	// find username
	filter := bson.M{"username": Name}
	err := collection.FindOne(context.TODO(), filter).Decode(&result)
	if err == nil {
		RtData := RtMsg {
			Msg: "Name has existed",
			Code: -1,
		}
		_, _ = ctx.JSON(RtData)
		return
	}

	// insert register data
	_, err = collection.InsertOne(context.TODO(), UserData)
	if err != nil {
		RtData := RtMsg {
			Msg: "Register error",
			Code: 1,
		}
		_, _ = ctx.JSON(RtData)
		return
	}

	RtData := RtMsg {
		Msg: "Register succeed",
		Code: 0,
	}
	_, _ = ctx.JSON(RtData)
}
