import java.util.*

fun main() {
    var (n, k) = readln().split(" ").map{ it.toInt() }
    val S = Stack<Int>()
    readln().forEach { c ->
        val m = c.code-48
        while (k > 0 && !S.isEmpty() && S.peek() < m) {
            S.pop()
            k--
        }
        S.push(m)
    }
    S.toList().subList(0,S.size-k).map(System.out::print)
}