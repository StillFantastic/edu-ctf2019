# m4chine

這題會拿到一個 pyc 檔，拿去反組譯後可以得到一段無法正確執行的 python 程式碼，經過一些修改後 (run.py) 使得他可以正確執行。接著嘗試理解程式碼的流程，基本上就是根據 machine code 對 輸入的字串進行操作，並且遇到 terminal 指令時最後一位必須不等於0。

於是就嘗試按照他的邏輯構造出一個字串，並且使得字串能夠通過他所有指令，需要特別注意的是當嘗試到最後幾個字時，會有多組解，此時根據 flag 有的特徵去構造即可。