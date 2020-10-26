package src

import (
	"context"
	"github.com/kataras/iris"
	"go.mongodb.org/mongo-driver/bson"
)

func Login(ctx iris.Context) {
	Username := ctx.FormValue("username")
	Password := ctx.FormValue("password")
	filter := bson.M{"username": Username}
	var result User
	collection := Client.Database("Pic").Collection("UserInfo")

	// find email
	err := collection.FindOne(context.TODO(), filter).Decode(&result)
	if err != nil {
		RtData := RtMsg {
			Msg: "Email does not exist",
			Code: -1,
		}
		_, _ = ctx.JSON(RtData)
		return
	}

	// check password
	if result.Password == Password {
		RtData := RtMsg {
			Msg: "Login success",
			Code: 1,
		}
		_, _ = ctx.JSON(RtData)
		return
	} else {
		RtData := RtMsg {
			Msg: "Wrong Password",
			Code: 0,
		}
		_, _ = ctx.JSON(RtData)
		return
	}
}
