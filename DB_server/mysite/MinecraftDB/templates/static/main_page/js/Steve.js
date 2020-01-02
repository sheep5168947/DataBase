function AttackAdder(add) {
    var hoe = add.toElement.id
    var spliter = hoe.split("-")
    var attack = spliter[1]
    var atkTable = ["0", "4", "4", "5", "6", "7", "9", "7", "7", "7", "9", "9", "9"]
    console.log(atkTable[attack])
}

var weapon1 = document.getElementById("weapon-1")
var weapon2 = document.getElementById("weapon-2")
var weapon3 = document.getElementById("weapon-3")
var weapon4 = document.getElementById("weapon-4")
var weapon5 = document.getElementById("weapon-5")
var weapon6 = document.getElementById("weapon-6")
var weapon7 = document.getElementById("weapon-7")
var weapon8 = document.getElementById("weapon-8")
var weapon9 = document.getElementById("weapon-9")
var weapon10 = document.getElementById("weapon-10")
var weapon11 = document.getElementById("weapon-11")
var weapon12 = document.getElementById("weapon-12")

weapon1.addEventListener("click", AttackAdder)
weapon2.addEventListener("click", AttackAdder)
weapon3.addEventListener("click", AttackAdder)
weapon4.addEventListener("click", AttackAdder)
weapon5.addEventListener("click", AttackAdder)
weapon6.addEventListener("click", AttackAdder)
weapon7.addEventListener("click", AttackAdder)
weapon8.addEventListener("click", AttackAdder)
weapon9.addEventListener("click", AttackAdder)
weapon10.addEventListener("click", AttackAdder)
weapon11.addEventListener("click", AttackAdder)
weapon12.addEventListener("click", AttackAdder)