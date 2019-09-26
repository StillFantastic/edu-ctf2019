# shellc0de

題目給了一個 c 語言原始碼，先花了一些時間搞懂原始碼內容，大致就是會執行輸入的機器碼，同時會卡一些組合，如`\x0f`、`\x00`、`\x05`。搞懂題目後花了兩三天學習組合語言，從 8086 到 x86 到 x64 都大約碰了一遍。

解題思路蠻清晰的，就是透過 syscall 去依序執行 open, read 還有 write, 至於卡掉的syscall 機器碼`\x0f \x05`則可以透過在記憶體中放置此指令減掉某些數字的結果，接著再用 `add` 去加回來。

過程中卡了一段時間，因為不知道寫的組合語言中其中一段使用`push`與手動`mov`進 stack 的差異為何，導致無法get flag，目前仍然還沒搞懂，待研究。

寫完組合語言後透過：
```
nasm -f bin read.asm
```
可以得到 binary 檔案，接著再透過
```
xxd -c 1 read | awk '{print "\\x"$2}' | tr -d '\n'
```
即可取得機器碼，最後
```
printf "machine code" | nc edu-ctf.csie.org 10150
```
順利得到 flag
