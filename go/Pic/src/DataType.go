package src


type User struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

type RtMsg struct {
	Msg string `json:"msg"`
	Code int `json:"code"`
}

type (
	FileList struct {
		List []FileInfo `json:"list"`
	}
)

type (
	FileInfo struct {
		FileName string `json:"file_name"`
		FileSize int64 `json:"file_size"`
	}
)