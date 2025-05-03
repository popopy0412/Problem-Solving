fun main() {
    var n = readln().toInt()
    var cnt = n/5
    var r = n%5
    while (r < n && r%2 != 0) {
        cnt--
        r+=5
    }
    println(if (r%2 == 0) cnt+r/2 else -1)
}