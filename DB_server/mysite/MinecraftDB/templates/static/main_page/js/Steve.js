function AttackAdder() {
    
    var atkTable = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0", "4", "4", "5", "6", "7", "9", "7", "7", "7", "9", "9", "9"]
   
    var mabiyoung = 0;

    for(var i=22;i<34;i++)
    {
        if(showheadimg[i].style.visibility=="visible")
        {
            mabiyoung = atkTable[i];
            break;
        }
    }
    ohnice.innerHTML=("Steve攻擊力")+mabiyoung
}

function DefendAdder() {
    console.log("fuck")
    var mabiyoung = 0;
    var atkTable = ["0","1","2","2","3","2","2","3","5","6","8","5","2","4","5","6","3","1","1","2","3","1"]
    for(var i=1;i<22;i++)
    {
        if(showheadimg[i].style.visibility=="visible")
        {
            mabiyoung += parseInt(atkTable[i]) ;
        }
    }
    
    ohsiht.innerHTML=("Steve防禦力:")+mabiyoung
}
 var ohsiht=document.querySelector(".hoewantthemoney1")
 var ohnice=document.querySelector(".hoewantthemoney2")



var head = document.getElementById("head");
var head_flag = 0;
var showheadimg = document.getElementById("Steve").children;
head.addEventListener("click", function () {
    var showhead = parseInt(event.target.id);
    if (head_flag == 0) {
        event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";

        showheadimg[showhead].style.visibility = "visible";
        
        head_flag = 1;
        
    } else if (head_flag == 1) {
        var str1 = "";
        str1 = event.target.style.boxShadow;
        if (str1 == "rgba(51, 51, 51, 0.5) 0px 3px 15px 3px") {
            event.target.style.boxShadow = "0 0 0 0";
            showheadimg[showhead].style.visibility = "hidden";
            head_flag = 0;
            
        } else {
            var child = head.children;
            for (var i = 0; i < child.length; i++) {
                child[i].style.boxShadow = '';
            }
            for (var i = 1; i < 7; i++) {
                showheadimg[i].style.visibility = "hidden";
            }
            showheadimg[showhead].style.visibility = "visible";
            event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
            head_flag = 1;
            
        }
    }
    DefendAdder();
})

var breast = document.getElementById("breast");
var breast_flag = 0;

breast.addEventListener("click", function () {
    var showhead = parseInt(event.target.id);
    if (breast_flag == 0) {
        event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
        showheadimg[showhead].style.visibility = "visible";
        breast_flag = 1;
        
    } else if (breast_flag == 1) {
        var str1 = "";
        str1 = event.target.style.boxShadow;
        if (str1 == "rgba(51, 51, 51, 0.5) 0px 3px 15px 3px") {
            event.target.style.boxShadow = "0 0 0 0";
            showheadimg[showhead].style.visibility = "hidden";
            breast_flag = 0;
            
        } else {
            var child = breast.children;
            for (var i = 0; i < child.length; i++) {
                child[i].style.boxShadow = '';
            }
            for (var i = 7; i < 12; i++) {
                showheadimg[i].style.visibility = "hidden";
            }
            showheadimg[showhead].style.visibility = "visible";
            event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
            breast_flag = 1;
            
        }

    }
    DefendAdder();

})


var leg = document.getElementById("leg");
var leg_flag = 0;
leg.addEventListener("click", function () {
    var showhead = parseInt(event.target.id);
    if (leg_flag == 0) {
        event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
        showheadimg[showhead].style.visibility = "visible";
        leg_flag = 1;
        
    } else if (leg_flag == 1) {
        var str1 = "";
        str1 = event.target.style.boxShadow;
        if (str1 == "rgba(51, 51, 51, 0.5) 0px 3px 15px 3px") {
            event.target.style.boxShadow = '0 0 0 0';
            showheadimg[showhead].style.visibility = "hidden";

            leg_flag = 0;
            
        } else {
            var child = leg.children;
            for (var i = 0; i < child.length; i++) {
                child[i].style.boxShadow = '';
            }
            for (var i = 12; i < 17; i++) {
                showheadimg[i].style.visibility = "hidden";
            }
            showheadimg[showhead].style.visibility = "visible";
            event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
            leg_flag = 1;
            
        }


    }
    DefendAdder();
})

var feet = document.getElementById("feet");
var feet_flag = 0;
feet.addEventListener("click", function () {
    var showhead = parseInt(event.target.id);
    if (feet_flag == 0) {
        event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
        showheadimg[showhead].style.visibility = "visible";
        feet_flag = 1;
        
    } else if (feet_flag == 1) {
        var str1 = "";
        str1 = event.target.style.boxShadow;
        if (str1 == "rgba(51, 51, 51, 0.5) 0px 3px 15px 3px") {
            event.target.style.boxShadow = '0 0 0 0';
            showheadimg[showhead].style.visibility = "hidden";
            feet_flag = 0;
            
        } else {
            var child = feet.children;
            for (var i = 0; i < child.length; i++) {
                child[i].style.boxShadow = '';
            }
            for (var i = 17; i < 22; i++) {
                showheadimg[i].style.visibility = "hidden";
            }
            showheadimg[showhead].style.visibility = "visible";
            event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
            feet_flag = 1;
            
        }

    }
    DefendAdder();
})

var weapon = document.getElementById("weapon");
var flag = 0;
weapon.addEventListener("click", function () {
    var showhead = parseInt(event.target.id);
    if (flag == 0) {
        event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
        showheadimg[showhead].style.visibility = "visible";
        flag = 1;
        
    } else if (flag == 1) {
        var str1 = "";
        str1 = event.target.style.boxShadow;
        if (str1 == "rgba(51, 51, 51, 0.5) 0px 3px 15px 3px") {
            showheadimg[showhead].style.visibility = "hidden";
            event.target.style.boxShadow = '';
            flag = 0;
            
        }

        else {
            var child = weapon.children;
            for (var i = 0; i < child.length; i++) {
                var child2 = child[i].children;
                for (var j = 0; j < child2.length; j++) {
                    var child3 = child2[j].children;
                    for (var k = 0; k < child3.length; k++) {
                        child3[k].style.boxShadow = '';
                    }
                }
            }
            for (var i = 22; i < 34; i++) {
                showheadimg[i].style.visibility = "hidden";
            }
            showheadimg[showhead].style.visibility = "visible";
            event.target.style.boxShadow = "0 3px 15px 3px rgba(51, 51, 51, 0.5)";
            flag = 1;
            
        }

    }
    AttackAdder()
})