fun main() {
    var (n,m) = readln().split(" ").map { it.toInt() }
    val l = Array(m) { readln().split(" ").map { it.toInt() }.let { (x,y) -> Pair(x,y) } }.sortedBy { it.first }
    val mi1 = l[0].first
    val mi2 = l.minByOrNull { it.second }!!.second
    var ans=0
    if (mi1 < mi2*6) {
        ans = n/6*mi1
        n%=6
    }
    ans += if (mi1*(n/6+(if (n%6>0) 1 else 0)) > mi2*n) mi2*n else mi1*(n/6+(if (n%6>0) 1 else 0))
    println(ans)
}