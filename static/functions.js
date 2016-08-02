function funct(n1, delt=1) {  
    var n2;
    var len = data.body[n1].length;
    n2 =  data.count[n1]
    n2 = (n2 + delt + len) % len;
    var tmp = data.intro[n1] + data.body[n1][n2];
    document.getElementById("ans" + n1).innerHTML = tmp;
    tmp = (n2 + 1)  + "/" + len;
    document.getElementById("page" + n1).innerHTML = tmp;
    data.count[n1] = n2;    
}

function home(list, mascot=false){
    var tmp;
    var len;
    var k;
    if (mascot == false){
        document.getElementById('mascot').style.display = "none";
    }
    else{
        document.getElementById('mascot').style.display = "inline";
    }
    document.getElementById('main').style.display = "none";
    document.getElementById("ans").innerHTML = '';
    //var list = [4,8,5,6];
    for(i=0; i<list.length; i++){
        data.count[list[i]] = -1;
        //tmp = "<span id=page" + i + "></span><div id=ans" + i + "></div><hr>";
        tmp = "<div id=ans" + list[i] + "></div><hr><br><br>";
        document.getElementById("ans").innerHTML += tmp;
        funct(list[i]);
    }
}

function index(){
    document.getElementById('mascot').style.display = "inline"; 
    document.getElementById("ans").innerHTML = '';
    document.getElementById('main').style.display = "inline";
}

function contact(){
    //document.getElementById('mascot').style.display = "inline"; 
    //document.getElementById("ans").innerHTML = '';
    //document.getElementById('main').style.display = "inline";
    var i = 11;
    data.count[i] = -1; 
    var tmp = "<div id=ans" + i + "></div><hr><br><br>";
    document.getElementById("ans").innerHTML = tmp;
    funct(i);
}

function test(){
    var n = 0;
    document.getElementById("ans").innerHTML = dat.body[n];
}
