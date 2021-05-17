import "jquery.min.js";
<!-- CryptoStego JS files.-->
import "../../src/sha512.js";
import "../../src/utf_8.js";
import "../../src/mersenne-twister.js";
import "../../src/utils.js";
import "../../src/readimg.js";
import "../../src/setimg.js";
import "../../src/main.js";
<!-- above scripts equivalent to <script type="text/javascript" src="cryptostego.min.js"></script>-->




function readIMG(){
    function readfunc(){
        var t=readMsgFromCanvas('canvas',$("#pass1").val(),0);
        if(t!=null){
            t=t.split('&').join('&amp;');
            t=t.split(' ').join('&nbsp;');
            t=t.split('<').join('&lt;');
            t=t.split('>').join('&gt;');
            t=t.replace(/(?:\r\n|\r|\n)/g, '<br />');
            $("#result").html(t);
        }else $("#result").html('ERROR REAVEALING MESSAGE!');

    }
    loadIMGtoCanvas('file1','canvas',readfunc);
}


document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('read');
    // onClick's logic below:
    link.addEventListener('click', function() {
        readIMG();
    });
});