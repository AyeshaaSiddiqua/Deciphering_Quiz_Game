window.onload = initall;
var saveAnsButton_A ;
var saveAnsButton_B ;
function initall() {
    saveAnsButton_A = document.getElementById('save_ans_A')
    saveAnsButton_A.onclick = save_ans_A;
    saveAnsButton_B = document.getElementById('save_ans_B')
    saveAnsButton_B.onclick = save_ans_B;
}

function save_ans_A() { 
    var r 
    r = confirm("Answer submitted go next");
    if(r == true) {
        var ans_A = $("input:radio[name=name]:checked").val()
        var url_A = '/save_ans_A?ans_A='+ans_A
        var req = new XMLHttpRequest();   
        req.open("GET", url_A, true);
        req.send();
    }
}

function save_ans_B() {
    var r  
    r = confirm("Answer submitted go next");
    if(r == true) {
        var ans_B = $("input:radio[name=name]:checked").val()
        var url_B = '/save_ans_B?ans_B='+ans_B
        var req = new XMLHttpRequest();   
        req.open("GET", url_B, true);
        req.send();
    }
}