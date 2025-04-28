var l: Array<IntArray> = emptyArray()
var n = 0
var m = 0
fun dfs(x: Int, y: Int): Boolean {
    l[x][y]=1
    if (y==m-1) return true
    val Y = arrayOf(-1,0,1)
    for (i in Y) {
        val (a, b) = Pair(x+i, y+1)
        if (a in 0 until n && l[a][b]==0 && dfs(a, b)) return true
    }
    return false
}

fun main() {
    var ans=0
    readln().split(" ").map { it.toInt() }.let { (a,b) -> n=a; m=b }
    l = Array(n) { readln().map { if (it=='.') 0 else 1 }.toIntArray() }
    for (i in 0 until n) if (dfs(i,0)) ans++
    println(ans)
}