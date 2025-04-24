import java.util.*
fun main() {
    val n = readln().toInt()
    val k = readln().toInt()
    val l = readln().split(" ").map { it.toInt() }.sorted()
    val pq = PriorityQueue<Int>(compareBy{-it})
    var ans=0
    for (i in 1 until n) {
        val t=l[i]-l[i-1]
        ans+=t
        pq.add(t)
    }
    repeat(k-1) { if (pq.isNotEmpty()) ans-=pq.poll() }
    println(ans)
}