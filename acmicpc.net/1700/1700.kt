import java.util.*

fun main() {
    var (n, k) = readln().split(" ").map { it.toInt() }
    val l: IntArray = readln().split(" ").map{ it.toInt() }.toIntArray()
    val s = Array<Queue<Int>>(k+1) { ArrayDeque() }
    val ck = IntArray(n)
    val check = IntArray(k+1)
    var q = n
    var ans = 0
    for (i in 0 until k) s[l[i]].add(i)
    for (i in 0 until k) {
        val m = l[i]
        s[m].poll()
        if (check[m] == 1) continue
        else if (q == 0) {
            var idx = 0
            if (s[ck[idx]].isNotEmpty()) {
                for (j in idx+1 until n) {
                    if (s[ck[j]].size == 0) {
                        idx = j
                        break
                    }
                    if (s[ck[j]].peek() > s[ck[idx]].peek()) idx = j
                }
            }
            check[ck[idx]]=0
            check[m]=1
            ck[idx]=m
            ans++
        } else {
            ck[n-q--]=m
            check[m]=1
        }
    }
    println(ans)
}