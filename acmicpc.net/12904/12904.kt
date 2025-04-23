fun main() {
    val a = readln()
    var b = StringBuilder(readln())
    val n = b.length - a.length

    for (i in 0 until n) {
        val m = b.length - 1
        val c = b[m]
        b.deleteCharAt(m)
        if (c =='B') {
            b = b.reversed() as StringBuilder
        }
    }

    println(if (a == b.toString()) 1 else 0)
}