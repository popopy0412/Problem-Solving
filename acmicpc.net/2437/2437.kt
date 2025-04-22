fun main() {
    var sum=0
    readln()
    readln().split(" ").map { it.toInt() }.sorted().forEach {
        if (it > sum+1) return@forEach
        sum+=it
    }
    println(sum+1)
}