fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val l = readln().split(" ").map { it.toLong() }.sorted().toLongArray()
    repeat(m) {
        val (x, y) = Pair(l[0], l[1])
        l[0] = x+y
        l[1] = x+y
        l.sort()
    }
    println(l.sum())
}