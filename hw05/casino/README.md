## Casino

閱讀完程式碼後可以很快發現在輸入名字的地方存在 buffer overflow，透過 checksec 可以發現 nx 跟 pie 都是 disabled 的，而且 GOT 也可寫。
接著尋找可以讓程式跳到 shellcode 的地方，發現在 guess 的地方沒有做範圍的判斷，所以可以透過負的索引值改到 GOT 表，而我選擇改寫 puts 函數的地址，這可以透過 readelf 或是 objdump 得到，進而讓程式遇到 puts 時會去執行在輸入名字處輸入的惡意代碼。
有一些細節例如 shellcode 可能會蓋到 seed 與 age 需要特別注意。
