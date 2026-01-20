# JableTVDownload

## 下載JableTV好幫手

每次看正要爽的時候就給我卡住轉圈圈

直接下載到電腦看沒煩惱

## 懶人包 for Windows 使用者

1. 請自行安裝 ffmpeg，裝完之後執行 INIT.bat 將會自動建置其餘環境。
2. 若收到可以執行 RUN.bat 之訊息，執行 RUN.bat 即可使用此神器。

### 1.搭建並啟用虛擬環境(Activate Virtual Environment)

```
python -m venv jable
jable/Scripts/activate
```
![image](https://github.com/hcjohn463/JableDownload/blob/main/img/createVenv.PNG)

### 2.下載所需套件、檔案(Download Requirement Files)
a.
`pip install -r requirements.txt`

![image](https://github.com/hcjohn463/JableDownload/blob/main/img/requirements.PNG)

b.
下載ChromeDriver至資料夾 [ChromeDriver]

![image](https://github.com/hcjohn463/JableDownload/blob/main/img/chromeDriver.PNG)

c.
安裝 [FFmpeg] 用於轉檔，此畫面代表FFmpeg安裝成功 (不安裝也可以看，不過影片會有拖拉卡幀的狀況)

![image](https://github.com/hcjohn463/JableDownload/blob/main/img/ffmpeg.png)

### 3.執行程式(Execute)
`python main.py`

### 4.輸入影片網址(Input Video Url)
`https://jable.tv/videos/ipx-486/`
![image](https://github.com/hcjohn463/JableDownload/blob/main/img/download2.PNG)

### 5.等待下載(Wait Download)
要轉檔輸入`y`，不要輸入`n`
要用GPU加速(Nvidia)轉檔輸入`y`，用CPU輸入`n`

![image](https://github.com/hcjohn463/JableDownload/blob/main/img/download.PNG)

### 6.等待轉檔(Wait Encode)
![image](https://github.com/hcjohn463/JableDownload/blob/main/img/encoding.png)

![image](https://github.com/hcjohn463/JableDownload/blob/main/img/encoded.png)

### 7.完成(Finish)
![image](https://github.com/hcjohn463/JableDownload/blob/main/img/demo2.png)

### 如果覺得好用 再麻煩給個星星好評 謝謝!!
---

[ChromeDriver]:<https://chromedriver.chromium.org/downloads>
[FFmpeg]:<https://www.ffmpeg.org/>

### Argument parser
`$python main.py -h`

![](https://i.imgur.com/qgyS5sf.png)

`$python main.py --random True`

可以直接下載隨機熱門影片

![](https://i.imgur.com/dSsdB7Y.png)

可以直接在cmd line指定url。

![](https://i.imgur.com/DKFrD7T.png)

### 更新日誌(Update log)
 🦕 2023/4/19 新增ffmpeg自動轉檔 v1.11
 🏹 2023/4/19 兼容Ubuntu Server v1.10
 🦅 2023/4/15 輸入演員鏈接，下載所有該演員相關的影片 v1.9
 🚗 2022/1/25 下載結束後抓封面 v1.8
 🐶 2021/6/4 更改m3u8得到方法(正則表達式) v1.7
 🌏 2021/5/28 更新代碼讓Unix系統(Mac,linux等)能使用 v1.6
 🍎 2021/5/27 更新爬蟲網頁方法 v1.5
 🌳 2021/5/20 修改編碼問題 v1.4
 🌈 2021/5/6 增加下載進度提示、修改Crypto問題 v1.3
 ⭐ 2021/5/5 更新穩定版本 v1.2
