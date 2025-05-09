var tree = LongArray(0)

fun update(i: Int, v: Long) {
    var i = i
    tree[i]=v
    while (i.also { i /= 2 } > 0) {
        tree[i] = tree[i*2] + tree[i*2+1]
    }
}

fun query(l: Int, r: Int, s: Int, e: Int, i: Int): Long {
    val mid = (l+r)/2
    return when {
        r < s || e < l -> 0
        s <= l && r <= e -> tree[i]
        else -> query(l, mid, s, e, i*2) + query(mid+1, r, s, e, i*2+1)
    }
}

fun main() = with(System.`in`.bufferedReader()){
    val (n, q) = readLine().split(" ").map { it.toInt() }
    val k = readLine().split(" ").map { it.toInt() }.toIntArray()
    var s = 1 shl (32-n.countLeadingZeroBits())
    if (s%n==0) s/=2
    tree = LongArray(2*s)
    for (i in 0..n-1) tree[s+i] = k[i].toLong()
    for (i in s-1 downTo 1) tree[i] = tree[i*2]+tree[i*2+1]
    repeat(q) {
        var (x, y, a, b) = readLine().split(" ").map { it.toInt() }
        if (x > y) {
            x = x xor y
            y = x xor y
            x = x xor y
        }
        println(query(1, s, x, y, 1))
        update(a+s-1, b.toLong())
    }
}