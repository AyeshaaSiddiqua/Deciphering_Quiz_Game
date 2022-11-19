window.onload = initall;
var  saveAnsButton ;
function initall() {
    saveAnsButton = document.getElementById('save_ans')
    saveAnsButton.onclick = save_ans;
}
function save_ans() {
    var r  
    r = confirm("Answer submitted go next");
    if(r == true) {
        var ans = $("input:radio[name=name]:checked").val()
        var url = '/save_ans?ans='+ans
        var req = new XMLHttpRequest();   
        req.open("GET", url, true);
        /**** req.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                saveAnsButton.onclick = document.getElementById("save_ans").disabled = true;
            }
            else{
                alert(this.status);
            }
          }; ****/
        req.send();
    }
}



